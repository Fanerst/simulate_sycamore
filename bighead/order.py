import networkx as nx
import numpy as np
import math
from scipy.special import logsumexp
import opt_einsum as oe
from copy import deepcopy
import kahypar
from os.path import join, dirname, abspath
from .utils import *
import math
from math import log2, log10
import opt_einsum as oe
import collections
import time
from .loadtensor import get_tensors
from traceback import print_exc
from sys import exit
import sys

"""
commandline example: 
python contraction_order.py -n 53 -m 14 -seed 0 -seed2 1 -simplify -seq ABCD -sc 39 -tc 42 -gpu_limit 30
"""


kahypar_profile_path = join(dirname(__file__), "config/cut_rKaHyPar_sea20.ini")


def edges_rearrange(edges, node_set):
    """
    convert node id of edges using a new indexing defined in node_set

    :param edges: list of tuples, such as [(35,3),(10,3)]
    :param node_set: list of node_ids, such as [35,10,3]

    :return edges_new: list of tuples, after convertion of node ids. Such as [(0,2),(1,2)]

    """
    edges_new = []
    for edge in edges:
        edges_new.append((node_set.index(edge[0]), node_set.index(edge[1])))
    return edges_new


def cut_size(adj, part):
    '''
    function for calculating cutsize of a subset of nodes

    :param adj: adjacence matrix of a graph
    :param parts: subset of vertices
    :return: cutsize
    '''
    return len(adj[part].nonzero()[0]) - len(adj[part][:, part].nonzero()[0])


def cut_size_shape(adj, part):
    '''
    function for calculating cutsize of a subset of nodes, but consider the weight 

    :param adj: weighted adjacence matrix of a graph
    :param parts: subset of vertices
    :return: cutsize
    '''
    return adj[part][adj[part].nonzero()].sum() - adj[part][:, part][adj[part][:, part].nonzero()].sum()

def kahypar_partition(edges, tn, node_set, adj, epsilon, K, seed=0):
    """
    using KaHyPar to divided node_set to two parts without given epsilon, epsilon will range from 0 to 1
    """
    n_v = len(node_set)
    hyperedge_indices = np.arange(0, len(edges) * 2 + 1, 2).tolist()
    hyperedges, edge_weights = [], []
    for edge in edges:
        idx0, idx1 = edge
        hyperedges += [idx0, idx1]
        node0, node1 = node_set[idx0], node_set[idx1]
        edge_weights.append(tn.shapes[node0][tn.neighbors[node0].index(node1)])
    hypergraph = kahypar.Hypergraph(n_v, len(edges), hyperedge_indices,
                                    hyperedges, K, edge_weights, [])
    context = kahypar.Context()
    context.loadINIconfiguration(kahypar_profile_path)
    context.setK(K)
    context.suppressOutput(True)
    context.setSeed(seed)
    context.setEpsilon(epsilon)
    kahypar.partition(hypergraph, context)
    partition = np.array([hypergraph.blockID(i) for i in hypergraph.nodes()])
    groups = [[node_set[idxi] for idxi in range(len(partition)) if partition[idxi] == t] for t in range(K)]

    # print(cutsize, tc, len(part0), len(part1), epsilon)
    return groups

def get_sc_tc(group, gsc, nins, nouts):
    sc2i = collections.defaultdict(list)
    i2tc = {}
    for i in group:
        sc1 = gsc - nouts[i] + nins[i]
        sc2 = nouts[i] + nins[i]
        sc = max(sc1,sc2)
        sc2i[sc].append(i)
        tc = gsc + nins[i]
        i2tc[i] = tc
    return sc2i, i2tc

def kickoff_group(group, tn, seed=0, n_trials=1):
    """
    Sperate function for kickoff method, which will kick off node one by one in group to get order. 

    Input:
    ======
    group: List, list of tensor ids that formulate a group for kickoffing
    tn: tensor network class, the given tensor network
    seed: Int, random number seed for Hahypar
    n_trials: Int, number of trials
    group: None or list, groups given or not

    Output:
    =======
    best_order: List of tuples, such as [(1,2),(3,4)], return best order given by kickoff
    best_scs: List of floats, space complexity of each step in best order given by kickoff
    best_tcs: List of floats, time complexity of each step in best order given by kickoff
    best_groups: List of ids, divided groups in the best order given by kickoff
    best_cutsize: Int, cutsize of the groups in the best order given by kickoff
    """
    N = len(tn.neighbors)
    G = nx.Graph()
    edges_weighted = []
    for edge in tn.edges:
        node0, node1 = edge
        weight = log2(tn.shapes[node0][tn.neighbors[node0].index(node1)])
        edges_weighted.append((node0, node1, weight))
    G.add_weighted_edges_from(edges_weighted)
    adj = nx.adjacency_matrix(G, nodelist=range(N))
    eps_list = np.arange(0.2, 0.82, 0.02).tolist()
    best_score = math.inf
    for eps in eps_list:
        # print('eps={:.2f}:'.format(eps)," seed=",seed)
        t0 = time.time()
        edges = edges_rearrange(list(G.subgraph(group).edges), group)
        group0, group1 = kahypar_partition(edges, tn, group, adj, eps, 2, seed)
        # print("kahypar time",time.time()-t0)
        # group0,group1 = groups
        cutsize01 = adj[group0][:, group1][adj[group0][:, group1].nonzero()].sum()
        cutsize0 = cut_size(adj, group0)
        cutsize1 = cut_size(adj, group1)
        mysc = max(cutsize0, cutsize1)
        mytc = cutsize0 + cutsize1 - cutsize01 + 1
        # print("nx cutsize=",mysc)
        id0 = min(group0)
        id1 = min(group1)
        myorder = [(id0,id1) if id0<id1 else (id1,id0)]
        for trial in range(n_trials):
            tcs = []
            scs = []
            order0,scs0,tcs0 = kickoff_group_sub(group0.copy(), tn, seed+trial)
            order1,scs1,tcs1 = kickoff_group_sub(group1.copy(), tn, seed+trial)
            tcs = tcs0+tcs1+[mytc]
            scs = scs0+scs1+[mysc]
            order = order0 + order1 + myorder
            tcs = [i for i in tcs]
            tc = log10sumexp2(tcs)
            sc = max(scs)
            score = score_fn(tc, sc)
            if score < best_score:
                best_score = score
                best_tc, best_sc = tc, sc
                best_order = order.copy()
                best_tcs = tcs.copy()
                best_scs = scs.copy()
                best_groups = [group0, group1]
                best_cutsize = mysc
            # print("trial",trial,"tc: {:.2f} ({:.2f}), sc: {:.1f}".format(tc,tc*log10(2), sc), best_tc)
        # print(eps, best_tc, best_sc, best_score)
    
    return best_order, best_scs, best_tcs, best_groups, best_cutsize

def kickoff_group_sub(group, tn, seed=0):
    """
    kickoff subroutine
    """
    rng = np.random.RandomState(seed)
    N = len(tn.neighbors)
    G = nx.Graph()
    edges_weighted = []
    for edge in tn.edges:
        node0, node1 = edge
        weight = log2(tn.shapes[node0][tn.neighbors[node0].index(node1)])
        edges_weighted.append((node0, node1, weight))
    G.add_weighted_edges_from(edges_weighted)
    adj = nx.adjacency_matrix(G, nodelist=range(N))
    gsc = cut_size(adj, group)
    nins = {}
    nouts = {}
    order = []
    scs = []
    tcs = []
    for i in group:
        nin = 0
        nout = 0
        for j in tn.neighbors[i]:
            shapeij = log2(tn.shapes[i][tn.neighbors[i].index(j)])
            if j in group:
                nin += shapeij
            else:
                nout += shapeij
        nins[i] = nin
        nouts[i] = nout

    for iter in range(len(group) - 1):
        sc2i,i2tc = get_sc_tc(group,gsc,nins,nouts)
        minsc = min(sc2i.keys())
        mintc = math.inf
        candi = []
        for j in sc2i[minsc]:
            if i2tc[j] < mintc:
                mintc = i2tc[j]
        candi = [i for i in sc2i[minsc] if abs(i2tc[i] - mintc)<0.01]
        i = rng.choice(candi)
        group.remove(i)
        j = min(group)

        order.insert(0,(i,j) if i<j else (j,i))
        tcs.insert(0,mintc)
        scs.insert(0,minsc)

        gsc = gsc - nouts[i] + nins[i]
        for j in tn.neighbors[i]:
            shapeij = log2(tn.shapes[i][tn.neighbors[i].index(j)])
            if j in group:
                nins[j] -= shapeij
                nouts[j] += shapeij

    return order, scs, tcs

class Contraction:
    def __init__(self, tensors, neighbors, shapes=None):
        """
        Tensor network class for finding contraction order
        """
        if tensors is None and shapes is None:
            raise ValueError('tensors and shapes could not all be None type')
        if shapes is None and tensors is not None:
            shapes = []
            for i in range(len(tensors)):
                if isinstance(tensors[i], list):
                    shapes.append([])
                else:
                    shapes.append(list(tensors[i].shape))

        self.tensors = tensors
        self.neighbors = {}.fromkeys(np.arange(len(neighbors)))
        self.shapes = {}.fromkeys(np.arange(len(shapes)))
        for key in self.neighbors.keys():
            self.neighbors[key] = neighbors[key]
            self.shapes[key] = shapes[key]

        self.edges = []
        for key in self.neighbors.keys():
            for node in self.neighbors[key]:
                if node > key:
                    self.edges.append((key, node))
        
    def _construct_edge_info(self, shapes, neighbors, strategy):
        edge_info = {}.fromkeys(self.edges)
        for edge in self.edges:
            edge_info = self._update_edge_info(edge, edge_info, shapes, neighbors, strategy)
        return edge_info

    def _update_edge_info(self, edge, edge_info, shapes, neighbors, strategy):
        m, n = edge
        idxm_n = neighbors[m].index(n)
        shapemn = shapes[m][idxm_n]
        shapem = prod(shapes[m])
        shapen = prod(shapes[n])
        if 'min_dim' in strategy:
            value = shapem * shapen / shapemn ** 2
        elif 'max_reduce' in strategy:
            value = shapem * shapen / shapemn ** 2 - (shapem + shapen)
        else:
            value = 1
        edge_info[edge] = value
        return edge_info

    def _add_edge_info(self, nodes, edge_info, shapes, neighbors, strategy):
        edges = []
        for node in nodes:
            for neighbor in neighbors[node]:
                if node > neighbor:
                    edge = (neighbor, node)
                else:
                    edge = (node, neighbor)
                if edge not in edges:
                    edges.append(edge)
                    self._update_edge_info(edge, edge_info, shapes, neighbors, strategy)
        return edge_info

    def _remove_edge_info(self, nodes, edge_info):
        edges = list(edge_info.keys())
        for edge in edges:
            if edge[0] in nodes or edge[1] in nodes:
                edge_info.pop(edge)
        return edge_info

    def contract_edge(self, edge, shapes, edge_info, neighbors, strategy):
        i, j = edge
        if (i, j) in edge_info.keys() or (j, i) in edge_info.keys():
            flag = True
        else:
            flag = False
        edge_info = self._remove_edge_info([i, j] + neighbors[i] + neighbors[j], edge_info)

        try:
            if flag:
                idxi_j = neighbors[i].index(j)
                idxj_i = neighbors[j].index(i)
                shapeij = shapes[i].pop(idxi_j)
                shapes[j].pop(idxj_i)
                neighbors[i].pop(idxi_j)
                neighbors[j].pop(idxj_i)
            else:
                shapeij = 1
            shapei, shapej = prod(shapes[i]), prod(shapes[j])
            for node in neighbors[j]:
                idxj_n = neighbors[j].index(node)
                idxn_j = neighbors[node].index(j)
                if node in neighbors[i]:
                    idxi_n = neighbors[i].index(node)
                    idxn_i = neighbors[node].index(i)
                    shapes[i][idxi_n] *= shapes[j][idxj_n]
                    shapes[node][idxn_i] *= shapes[node][idxn_j]
                    shapes[node].pop(idxn_j)
                    neighbors[node].pop(idxn_j)
                else:
                    shapes[i].append(shapes[j][idxj_n])
                    neighbors[i].append(node)
                    neighbors[node][idxn_j] = i
        except:
            print('error when contract {} and {}'.format(i, j))
            print(neighbors[i], len(shapes[i]), len(neighbors[i]))
            print(neighbors[j], len(shapes[j]), len(neighbors[j]))
            for node in neighbors[j]:
                print(node, neighbors[node], shapes[node])
            print_exc()
            exit(0)
        neighbors[j] = []
        shapes[j] = []

        edge_info = self._add_edge_info([i] + neighbors[i], edge_info, shapes, neighbors, strategy)

        return shapei * shapeij * shapej, shapes, edge_info, neighbors

    def _edge_select(self, strategy, edge_info, neighbors, edge_pool=None):
        if edge_pool is not None:
            edge_info = {edge: edge_info[edge] for edge in edge_pool}
        min_value = min(edge_info.values())
        min_edges = [edge for edge in edge_info.keys() if edge_info[edge] == min_value]
        if 'tri' in strategy:
            triangle_count = []
            for edge in min_edges:
                m, n = edge
                triangle_count.append(len(np.intersect1d(np.array(neighbors[m]), np.array(neighbors[n]))))
            tc = np.array(triangle_count)
            edge = min_edges[self.rng.choice(np.argwhere(tc == tc.max()).reshape(-1))]
        else:
            edge = min_edges[self.rng.choice(np.arange(len(min_edges)))]
        return edge

    def contraction(self, strategy='min_dim', order=None, communities=None, seed=0):
        self.rng = np.random.RandomState(seed)
        if order is None:
            order = []
        else:
            strategy = 'predefined'
        shapes = deepcopy(self.shapes)#shapes = self.shapes.copy()
        neighbors = deepcopy(self.neighbors)# neighbors = self.neighbors.copy()
        edge_info = self._construct_edge_info(shapes, neighbors, strategy)
        time_complexity = []
        space_complexity = [max([math.log2(prod(shapes[i])) for i in range(len(shapes))])]

        if communities is not None:
            for com in communities:
                edge_pool = [edge for edge in edge_info.keys() if edge[0] in com and edge[1] in com]
                if len(edge_pool) == 0:
                    continue
                while True:
                    # edge_pool = [edge for edge in edge_info.keys() if edge[0] in com and edge[1] in com]
                    edge = self._edge_select(strategy, edge_info, neighbors, edge_pool)
                    order.append(edge)
                    tc_step, shapes, edge_info, neighbors = self.contract_edge(edge,
                                                                               shapes,
                                                                               edge_info,
                                                                               neighbors,
                                                                               strategy)
                    time_complexity.append(math.log2(tc_step))
                    space_complexity.append(max(space_complexity[-1], math.log2(prod(shapes[edge[0]]))))
                    i, j = edge
                    edge_pool.remove(edge)
                    if len(edge_pool) == 0:
                        break
                    for l in range(len(edge_pool)):
                        if j in edge_pool[l]:
                            k = edge_pool[l][edge_pool[l].index(j)==0]
                            if i < k:
                                edge_pool[l] = (i, k)
                            else:
                                edge_pool[l] = (k, i)
                    edge_pool = list(set(edge_pool))

        while len(edge_info) > 0:
            if strategy == 'predefined':
                edge = order.pop(0)
            else:
                edge = self._edge_select(strategy, edge_info, neighbors)
                order.append(edge)
            tc_step, shapes, edge_info, neighbors = self.contract_edge(edge, shapes, edge_info, neighbors, strategy)
            time_complexity.append(math.log2(tc_step))
            space_complexity.append(max(space_complexity[-1], math.log2(prod(shapes[edge[0]]))))
            
        tc = log10sumexp2(time_complexity) # / math.log(10)
        sc = max(space_complexity)

        return tc, sc, time_complexity, space_complexity, order
    
    def contraction_partorder(self, order):
        strategy = 'predefined'
        shapes = deepcopy(self.shapes)#shapes = self.shapes.copy()
        neighbors = deepcopy(self.neighbors)# neighbors = self.neighbors.copy()
        edge_info = self._construct_edge_info(shapes, neighbors, strategy)
        time_complexity = []
        space_complexity = [] # [max([math.log2(prod(shapes[i])) for i in range(len(shapes))])]
        for edge in order:
            tc_step, shapes, edge_info, neighbors = self.contract_edge(edge, shapes, edge_info, neighbors, strategy)
            time_complexity.append(math.log2(tc_step))
            space_complexity.append(math.log2(prod(shapes[edge[0]])))# space_complexity.append(max(space_complexity[-1], math.log2(prod(shapes[edge[0]]))))
        tc = log10sumexp2(time_complexity)
        sc = max(space_complexity)

        return tc, sc, time_complexity, space_complexity, neighbors, shapes

    def contraction_communities(self, communities, strategy='min_dim', seed=0):
        self.rng = np.random.RandomState(seed)
        order = []
        shapes = deepcopy(self.shapes)#shapes = self.shapes.copy()
        neighbors = deepcopy(self.neighbors)# neighbors = self.neighbors.copy()
        edge_info = self._construct_edge_info(shapes, neighbors, strategy)
        time_complexity = []
        space_complexity = [max([math.log2(prod(shapes[i])) for i in range(len(shapes))])]

        for com in communities:
            edge_pool = [edge for edge in edge_info.keys() if edge[0] in com and edge[1] in com]
            if len(edge_pool) == 0:
                continue
            while True:
                # edge_pool = [edge for edge in edge_info.keys() if edge[0] in com and edge[1] in com]
                edge = self._edge_select(strategy, edge_info, neighbors, edge_pool)
                order.append(edge)
                tc_step, shapes, edge_info, neighbors = self.contract_edge(edge,
                                                                           shapes,
                                                                           edge_info,
                                                                           neighbors,
                                                                           strategy)
                time_complexity.append(math.log(tc_step))
                space_complexity.append(max(space_complexity[-1], math.log2(prod(shapes[edge[0]]))))
                i, j = edge
                edge_pool.remove(edge)
                if len(edge_pool) == 0:
                    break
                for l in range(len(edge_pool)):
                    if j in edge_pool[l]:
                        k = edge_pool[l][edge_pool[l].index(j)==0]
                        if i < k:
                            edge_pool[l] = (i, k)
                        else:
                            edge_pool[l] = (k, i)
                edge_pool = list(set(edge_pool))

        return time_complexity, space_complexity, order
    
    def contraction_one_community(self, community, strategy='min_dim', seed=0):
        self.rng = np.random.RandomState(seed)
        order = []
        shapes = deepcopy(self.shapes)#shapes = self.shapes.copy()
        neighbors = deepcopy(self.neighbors)# neighbors = self.neighbors.copy()
        edge_info = self._construct_edge_info(shapes, neighbors, strategy)
        time_complexity = []
        space_complexity = [max([math.log2(prod(shapes[i])) for i in range(len(shapes))])]

        edge_pool = [edge for edge in edge_info.keys() if edge[0] in community and edge[1] in community]
        if len(edge_pool) == 0:
            return time_complexity, space_complexity, order
        while True:
            # edge_pool = [edge for edge in edge_info.keys() if edge[0] in com and edge[1] in com]
            edge = self._edge_select(strategy, edge_info, neighbors, edge_pool)
            order.append(edge)
            tc_step, shapes, edge_info, neighbors = self.contract_edge(edge,
                                                                        shapes,
                                                                        edge_info,
                                                                        neighbors,
                                                                        strategy)
            time_complexity.append(math.log2(tc_step))
            space_complexity.append(max(space_complexity[-1], math.log2(prod(shapes[edge[0]]))))
            i, j = edge
            edge_pool.remove(edge)
            for l in range(len(edge_pool)):
                if j in edge_pool[l]:
                    k = edge_pool[l][edge_pool[l].index(j)==0]
                    if i < k:
                        edge_pool[l] = (i, k)
                    else:
                        edge_pool[l] = (k, i)
            edge_pool = list(set(edge_pool))
            if len(edge_pool) == 0:
                if len(order) == len(community) - 1:
                    break
                else:
                    involved_nodes = set()
                    for edge in order:
                        # involved_nodes.add(edge[0])
                        involved_nodes.add(edge[1])
                    uninvolved_nodes = set(community) - involved_nodes
                    source_node = order[-1][0]
                    for node in uninvolved_nodes:
                        if node == source_node:
                            continue
                        edge = (source_node, node)
                        order.append(edge)
                        tc_step, shapes, edge_info, neighbors = self.contract_edge(edge,
                                                                                    shapes,
                                                                                    edge_info,
                                                                                    neighbors,
                                                                                    strategy)
                        time_complexity.append(math.log2(tc_step))
                        space_complexity.append(max(space_complexity[-1], math.log2(prod(shapes[edge[0]]))))
                    break

        return time_complexity, space_complexity, order

    def _labels_to_einsum(self, group=None, shapes=None):
        """
        return the einsum equation corresponding to the tensor network contraction        
        """
        if group is None:
            group = range(len(self.neighbors))
        if shapes is None:
            shapes = self.shapes
        eq = ''
        out_inds = ''
        insets = []
        sizes = []
        idx_sizes = {}
        for i in group:
            neigh = self.neighbors[i]
            shape_tmp = []
            eq_tmp = ''
            for j in neigh:
                if j < i:
                    index = self.edges.index((j, i))
                else:
                    index = self.edges.index((i, j))
                symbol = oe.get_symbol(index)
                if j not in group:
                    out_inds += symbol
                eq_tmp += symbol
                size = shapes[i][neigh.index(j)]
                shape_tmp.append(size)
                idx_sizes.setdefault(symbol, size)
            sizes.append(shape_tmp)
            insets.append(list(eq_tmp))
            eq += eq_tmp
            eq += ','
        eq = eq[:len(eq) - 1] + '->' + out_inds

        return eq, sizes, insets, idx_sizes

    def kahypar_parition(self, edges, node_set, adj, epsilons, cutsize_target, tc_target, seed=0):
        """
        using KaHyPar to divided node_set to two parts with given epsilon or (list of epsilon) to meet given targets
        """
        n_v = len(node_set)
        hyperedge_indices = np.arange(0, len(edges) * 2 + 1, 2).tolist()
        hyperedges, edge_weights = [], []
        for edge in edges:
            idx0, idx1 = edge
            hyperedges += [idx0, idx1]
            node0, node1 = node_set[idx0], node_set[idx1]
            edge_weights.append(self.shapes[node0][self.neighbors[node0].index(node1)])
            # hyperedges += [edge[0], edge[1]]
            # edge_weights.append(self.shapes[edge[0]][self.neighbors[edge[0]].index(edge[1])])
        hypergraph = kahypar.Hypergraph(n_v, len(edges), hyperedge_indices,
                                        hyperedges, 2, edge_weights, [])
        if type(epsilons) is not list:
            epsilons = [epsilons]
        for epsilon in epsilons:
            context = kahypar.Context()
            context.loadINIconfiguration(kahypar_profile_path)
            context.setK(2)
            context.suppressOutput(True)
            context.setSeed(seed)
            context.setEpsilon(epsilon)
            kahypar.partition(hypergraph, context)
            partition = np.array([hypergraph.blockID(i) for i in hypergraph.nodes()])
            part0 = np.array(node_set)[np.nonzero(-partition + 1)].tolist()
            part1 = np.array(node_set)[np.nonzero(partition)].tolist()
            assert len(part0) + len(part1) == n_v
            # cutsize0, cutsize1 = cut_size(adj, part0), cut_size(adj, part1)
            # cutsize01 = len(adj[part0][:, part1].nonzero()[0])
            cutsize0, cutsize1 = cut_size_shape(adj, part0), cut_size_shape(adj, part1)
            cutsize01 = adj[part0][:, part1][adj[part0][:, part1].nonzero()].sum()
            # cutsize_kahypar = kahypar.cut(hypergraph)
            # print('cutsize:', cutsize_kahypar, cutsize01)
            cutsize, tc = max(cutsize0, cutsize1), cutsize0 + cutsize1 - cutsize01
            if cutsize <= cutsize_target and tc <= tc_target:
                flag = True
                break
            else:
                flag = False
        if flag or epsilon >= 1.0:
            print(cutsize, tc, len(part0), len(part1), epsilon, seed)
        
        return flag, part0, part1

    def bipartition(self, cutsize_target=34, tc_target=44, seed=0):
        """
        Frist, divide nodes into two groups hierarchically until size of each group is smaller than a threshold.
        Second, contract each group, then contract the remaining contraction tree layer by layer using the order speficied by the hierarchical partitioning.

        Input:
        ======
        cutsize_target: Int, each bi-partition must give a sc smaller than cutsize_target
        tc_target: Float, each bi-partition must give a log2(tc) smaller than tc_target
        seed: Int, random number seed for Hahypar

        Output:
        =======
        orders: List of tuples, such as [(1,2),(3,4)]
        parts: list of list, the final division after hierarchical partitioning.  
                Each group contains set of nodes of G. Such as [[1,2,3],[4,5,6]]
        if the order meet target not found, None type will be returned

        """
        N = len(self.neighbors)
        node_set = [i for i in range(N)]
        G = nx.Graph()
        edges_weighted = []
        for edge in self.edges:
            node0, node1 = edge
            weight = math.log2(self.shapes[node0][self.neighbors[node0].index(node1)])
            edges_weighted.append((node0, node1, weight))
        G.add_weighted_edges_from(edges_weighted)
        adj = nx.adjacency_matrix(G, nodelist=range(N))
        for trial in range(20):
            orders = []
            print('trials {}:'.format(trial+1))
            e = (0.1 * trial) / 5 + 0.8 # 0.02 * trial #
            flag, part0, part1 = self.kahypar_parition(self.edges, node_set, adj, e, cutsize_target, tc_target, trial)
            part_top = [part0, part1]
            if flag:
                order_append, parts = partition2order([part0, part1], G, adj)
                orders = order_append + orders
            else:
                continue
            while True:
                length_com = [int(len(part) <= 60) for part in parts]
                print(length_com, orders)
                if sum(length_com) == len(parts):
                    _, _, order_com = self.contraction_communities(parts,
                                                                   strategy="max_reduce_tri",
                                                                   seed=10)
                    orders = order_com + orders
                    return orders, parts, part_top, nx.cut_size(G, part_top[0])
                else:
                    idx = np.argwhere(np.array(length_com)==0)[0][0]
                    part = parts[idx]
                    edges = edges_rearrange(list(G.subgraph(part).edges), part)
                    for eps in np.arange(0, 1.02, 0.02):
                        flag, part0, part1 = self.kahypar_parition(edges, part, adj, eps, cutsize_target, tc_target, seed)
                        if flag:
                            break
                    if flag:
                        order_append, parts_new = partition2order([part0, part1], G, adj)
                        orders = order_append + orders
                        parts.pop(idx)
                        parts += parts_new
                    else:
                        break
        
        return None
    
    def order_kickoff(self, sc_target=34, tc_target=38, seed=0, n_trials=1, groups=None):
        """
        Divide nodes into two groups groups, then kick off node one by one in each group.
        If groups are given, then aviod the bipartition step.

        Input:
        ======
        sc_target: Int, each bi-partition must give a sc smaller than sc_target
        tc_target: Float, each bi-partition must give a log2(tc) smaller than tc_target
        seed: Int, random number seed for Hahypar
        n_trials: Int, number of trials
        groups: None or list, groups given or not

        Output:
        =======
        best_order: List of tuples, such as [(1,2),(3,4)], return best order given by kickoff
        best_scs: List of floats, space complexity of each step in best order given by kickoff
        best_tcs: List of floats, time complexity of each step in best order given by kickoff
        """
        N = len(self.neighbors)
        node_set = [i for i in range(N)]
        G = nx.Graph()
        for edge in self.edges:
            G.add_edge(edge[0], edge[1])
        adj = nx.adjacency_matrix(G, nodelist=range(N))
        eps_list = np.arange(0, 1.1, 0.1).tolist()
        best_tc = math.inf
        if groups is None:
            for eps in eps_list:
                print('eps={:.2f}:'.format(eps)," seed=",seed)
                
                t0=time.time()
                groups = kahypar_partition(self.edges, self, node_set, adj, 2, seed,eps)
                print("kahypar time",time.time()-t0)
                group0,group1 = groups
                mysc = nx.cut_size(G,group0,group1)
                mytc = mysc
                print("nx cutsize=",mysc)
                id0 = min(group0)
                id1 = min(group1)
                myorder = [(id0,id1) if id0<id1 else (id1,id0)]
                for trial in range(n_trials):
                    tcs = []
                    scs = []
                    order0,scs0,tcs0 = kickoff_group_sub(group0.copy(), self, seed+trial)
                    order1,scs1,tcs1 = kickoff_group_sub(group1.copy(), self, seed+trial)
                    tcs = tcs0+tcs1+[mytc]
                    scs = scs0+scs1+[mysc]
                    order = order0 + order1 + myorder
                    tcs = [i*math.log(2) for i in tcs]
                    tc = logsumexp(tcs) /math.log(2.)
                    sc = max(scs)
                    if tc < best_tc:
                        best_tc = tc
                        best_order = order.copy()
                        best_tcs = tcs.copy()
                        best_scs = scs.copy()
                    print("trial",trial,"tc: {:.2f} ({:.2f}), sc: {:.1f}".format(tc,tc*math.log(2)/math.log(10), sc))
        else:
            group0,group1 = groups
            mysc = nx.cut_size(G,group0,group1)
            mytc = mysc
            print("nx cutsize=",mysc)
            id0 = min(group0)
            id1 = min(group1)
            myorder = [(id0,id1) if id0<id1 else (id1,id0)]
            for trial in range(n_trials):
                tcs = []
                scs = []
                order0,scs0,tcs0 = kickoff_group_sub(group0.copy(), self, seed+trial)
                order1,scs1,tcs1 = kickoff_group_sub(group1.copy(), self, seed+trial)
                tcs = tcs0+tcs1+[mytc]
                scs = scs0+scs1+[mysc]
                order = order0 + order1 + myorder
                tcs = [i*math.log(2) for i in tcs]
                tc = logsumexp(tcs) /math.log(2.)
                sc = max(scs)
                if tc < best_tc:
                    best_tc = tc
                    best_order = order.copy()
                    best_tcs = tcs.copy()
                    best_scs = scs.copy()
                print("trial",trial,"tc: {:.2f} ({:.2f}), sc: {:.1f}".format(tc,tc*math.log(2)/math.log(10), sc))

        return best_order, best_scs, best_tcs

    def order_kickoff3(self, sc_target=34, tc_target=38, seed=0, n_trials=1):
        """
        Divide nodes into three groups, then kick off node one by one in each group.
        If groups are given, then aviod the bipartition step.

        Input:
        ======
        sc_target: Int, each bi-partition must give a sc smaller than sc_target
        tc_target: Float, each bi-partition must give a log2(tc) smaller than tc_target
        seed: Int, random number seed for Hahypar
        n_trials: Int, number of trials

        Output:
        =======
        best_order: List of tuples, such as [(1,2),(3,4)], return best order given by kickoff
        best_scs: List of floats, space complexity of each step in best order given by kickoff
        best_tcs: List of floats, time complexity of each step in best order given by kickoff
        """
        N = len(self.neighbors)
        node_set = [i for i in range(N)]
        G = nx.Graph()
        for edge in self.edges:
            G.add_edge(edge[0], edge[1])
        adj = nx.adjacency_matrix(G, nodelist=range(N))
        eps_list = np.arange(0, 1.1, 0.1).tolist()
        best_tc = math.inf
        for eps in eps_list:
            print('eps={:.2f}:'.format(eps)," seed=",seed)
            t0=time.time()
            groups = kahypar_partition(self.edges, node_set, adj, 3, seed,eps)
            print("kahypar time",time.time()-t0)
            group0,group1,group2 = groups
            cut01 = nx.cut_size(G,group0,group1)
            cut02 = nx.cut_size(G,group0,group2)
            cut12 = nx.cut_size(G,group1,group2)
            size0 = cut01+cut02
            size1 = cut01+cut12
            size2 = cut02+cut12
            mysc = max(size0,size1,size2)
            sc1=cut01+cut02+cut12
            max_cut = max(cut01,cut02,cut12)
            sc2 = sc1 - max_cut
            mytc = logsumexp([sc1*math.log(2.),sc2*math.log(2.)])/math.log(2.)
    #        print("nx cutsize=",mysc)
            print("top tc=",mysc)
            id0 = min(group0)
            id1 = min(group1)
            id2 = min(group2)
            # myorder = [(id0,id1),(id0,id2)] # this is a temporary one
            if cut01 == max_cut:
                myorder = [(id0, id1), (id0, id2)]
            elif cut02 == max_cut:
                myorder = [(id0, id2), (id0, id1)]
            else:
                myorder = [(id1, id2), (id0, id1)]
            for trial in range(n_trials):
                tcs = []
                scs = []
                order = []
                for group in groups:
                    order0,scs0,tcs0 = kickoff_group(G,group.copy(),seed+trial)
                    tcs += tcs0
                    scs += scs0
                    order += order0
                tcs.append(mytc)
                scs.append(mysc)
                order += myorder
                tcs = [i*math.log(2) for i in tcs]
                tc = logsumexp(tcs) /math.log(2.)
                sc = max(scs)
                if tc < best_tc:
                    best_tc = tc
                    best_order = order.copy()
                    best_tcs = tcs.copy()
                    best_scs = scs.copy()
                print("trial",trial,"tc: {:.2f} ({:.2f}), sc: {:.1f}".format(tc,tc*math.log(2)/math.log(10), sc))

        return best_order,best_scs,best_tcs

    def bipartition1(self, cutsize_target=34, tc_target=44, seed=0):
        """
        Frist, divide nodes into two groups hierarchically until size of each group is smaller than a threshold.
        Second, contract each group, then contract the remaining contraction tree layer by layer using the order speficied by the hierarchical partitioning.

        Input:
        ======
        sc_target: Int, each bi-partition must give a sc smaller than sc_target
        tc_target: Float, each bi-partition must give a log2(tc) smaller than tc_target
        seed: Int, random number seed for Hahypar

        Output:
        =======
        orders: List of tuples, such as [(1,2),(3,4)]
        parts: list of list, the final division after hierarchical partitioning.  
                Each group contains set of nodes of G. Such as [[1,2,3],[4,5,6]]
        if the order meet target not found, None type will be returned

        """
        N = len(self.neighbors)
        node_set = [i for i in range(N)]
        G = nx.Graph()
        edges_weighted = []
        for edge in self.edges:
            node0, node1 = edge
            weight = math.log2(self.shapes[node0][self.neighbors[node0].index(node1)])
            edges_weighted.append((node0, node1, weight))
        G.add_weighted_edges_from(edges_weighted)
        adj = nx.adjacency_matrix(G, nodelist=range(N))
        for trial in range(15):
            orders = []
            print('trials {}:'.format(trial+1))
            e = 0.7 + 0.02 * trial # (0.1 * trial) / 5 + 0.8 #
            flag, part0, part1 = self.kahypar_parition(self.edges, node_set, adj, e, cutsize_target, tc_target, trial)
            groups0 = [part0, part1]
            cutsize0 = nx.cut_size(G, part0, part1)
            if flag:
                order_append, _ = partition2order([part0, part1], G, adj)
                orders = order_append + orders
                parts = [[part0], [part1]]
            else:
                continue
            order_bipart = [[], []]
            flags = [False, False]
            for k in range(2):
                while True:
                    length_com = [int(len(part) <= 60) for part in parts[k]]
                    print(k, length_com, order_bipart[k], len(parts[k]))
                    if sum(length_com) == len(parts[k]):
                        _, _, order_com = self.contraction_communities(parts[k],
                                                                       strategy="max_reduce_tri",
                                                                       seed=10)
                        order_bipart[k] = order_com + order_bipart[k]
                        flags[k] = True
                        break
                    else:
                        idx = np.argwhere(np.array(length_com)==0)[0][0]
                        part = parts[k][idx]
                        edges = edges_rearrange(list(G.subgraph(part).edges), part)
                        for eps in np.arange(0, 1.02, 0.02):
                            flag, part0, part1 = self.kahypar_parition(edges, part, adj, eps, cutsize_target, tc_target, seed)
                            if flag:
                                break
                        # flag, part0, part1 = self.kahypar_parition(edges, part, adj, cutsize_target, tc_target, seed)
                        if flag:
                            order_append, parts_new = partition2order([part0, part1], G, adj)
                            order_bipart[k] = order_append + order_bipart[k]
                            parts[k].pop(idx)
                            parts[k] += parts_new
                        else:
                            break
            if flags[0] and flags[1]:
                orders = order_bipart[0] + order_bipart[1] + orders
                return orders, parts[0] + parts[1], 1, groups0, cutsize0

        return None
    
def slicing_partorder_complexity(neighbors, shapes, order, slicing_edge=None):
    """
    return contraction complexity of given tensor network, order and probably slicing edges
    """
    neighbors_new = deepcopy(neighbors)
    shapes_new = deepcopy(shapes)
    if slicing_edge is not None:
        if type(slicing_edge) is tuple:
            slicing_edge = [slicing_edge]
        for edge in slicing_edge:
            i, j = edge
            if i in neighbors_new[j] and j in neighbors_new[i]:
                idxi_j = neighbors_new[i].index(j)
                idxj_i = neighbors_new[j].index(i)
                shapes_new[i][idxi_j] = 1
                shapes_new[j][idxj_i] = 1
            else:
                raise ValueError('({}, {}) is not a valid edge'.format(i, j))
    time_complexity = []
    space_complexity = [max([math.log2(prod(shapes_new[i])) for i in range(len(shapes_new))])]
    for edge in order:
        i, j = edge
        if i in neighbors_new[j] and j in neighbors_new[i]:
            flag = True
        else:
            flag = False
        try:
            if flag:
                idxi_j = neighbors_new[i].index(j)
                idxj_i = neighbors_new[j].index(i)
                shapeij = shapes_new[i].pop(idxi_j)
                shapes_new[j].pop(idxj_i)
                neighbors_new[i].pop(idxi_j)
                neighbors_new[j].pop(idxj_i)
            else:
                shapeij = 1
            shapei, shapej = prod(shapes_new[i]), prod(shapes_new[j])
            for node in neighbors_new[j]:
                idxj_n = neighbors_new[j].index(node)
                idxn_j = neighbors_new[node].index(j)
                if node in neighbors_new[i]:
                    idxi_n = neighbors_new[i].index(node)
                    idxn_i = neighbors_new[node].index(i)
                    shapes_new[i][idxi_n] *= shapes_new[j][idxj_n]
                    shapes_new[node][idxn_i] *= shapes_new[node][idxn_j]
                    shapes_new[node].pop(idxn_j)
                    neighbors_new[node].pop(idxn_j)
                else:
                    shapes_new[i].append(shapes_new[j][idxj_n])
                    neighbors_new[i].append(node)
                    neighbors_new[node][idxn_j] = i
        except:
            raise ValueError('error when contract {} and {}'.format(i, j))
        neighbors_new[j] = []
        shapes_new[j] = []
        
        tc_step = shapei * shapeij * shapej
        time_complexity.append(math.log2(tc_step))
        space_complexity.append(max(space_complexity[-1], math.log2(prod(shapes_new[edge[0]]))))
    tc = log10sumexp2(time_complexity)
    sc = max(space_complexity)

    return tc, sc, time_complexity, space_complexity


def partition2order(parts, G, adj):
    """
    given two partitions, return the order of contracting them to one part
    """
    assert len(parts) == 2
    parts_new = []
    for i in range(2):
        ccs = list(nx.connected_components(nx.subgraph(G, parts[i])))
        for cc in ccs:
            parts_new.append(list(cc))
        
    node_rep = [min(cc) for cc in parts_new]
    L = len(node_rep)
    idx = np.argsort(node_rep)
    node_rep.sort()
    if L == 2:
        order_append = [(node_rep[0], node_rep[1])]
    else:
        print("Not 2!")
        tmp = [parts_new[n] for n in idx]
        neigh = []
        shapes = []
        for n in range(len(tmp)):
            neigh_tmp = []
            shape_tmp = []
            for m in range(len(tmp)):
                if n == m:
                    continue
                shape = len(adj[tmp[n]][:, tmp[m]].nonzero()[0])
                if shape != 0:
                    neigh_tmp.append(m)
                    shape_tmp.append(shape)
            if len(neigh_tmp) != 0:
                neigh.append(neigh_tmp)
                shapes.append(shape_tmp)
        # print(neigh, shapes)
        con = Contraction(None, neigh, shapes)
        _, _, _, _, order_tmp = con.contraction(strategy='max_reduce_tri', seed=0)
        order_append = [(node_rep[edge[0]], node_rep[edge[1]]) for edge in order_tmp]
    
    return order_append, parts_new

def cut_size(adj, part1, part2=None):
    if part2:
        cutsize = adj[part1][:, part2][adj[part1][:, part2].nonzero()].sum()
    else:
        cutsize = adj[part1][adj[part1].nonzero()].sum() - adj[part1][:, part1][adj[part1][:, part1].nonzero()].sum()
    return cutsize

def score_fn(tc, sc):
    """
    Score function for finding order
    """
    return tc + sc * log10(2)

class ContractionVertex:
    def __init__(self, contain_nodes, parent, left, right) -> None:
        """
        Class of contraction vertex
        """
        self.contain_nodes = contain_nodes
        self.parent = parent
        self.left = left
        self.right = right

class ContractionTree:
    def __init__(self, neighbors, shapes, order, edges=None, seed=0) -> None:
        """
        Class of contraction tree
        """
        self.order = order
        self.adj = np.zeros([len(neighbors), len(neighbors)])
        if edges:
            self.edges = edges
            construct_edges = False
        else:
            self.edges = []
            construct_edges = True
        for i in range(len(neighbors)):
            for j in range(len(neighbors[i])):
                if i < neighbors[i][j]:
                    self.adj[i, neighbors[i][j]] = self.adj[neighbors[i][j], i] = log2(shapes[i][j])
                    if construct_edges:
                        self.edges.append((i, neighbors[i][j]))
        self.neighbors = neighbors
        self.shapes = shapes
        self.all_nodes = frozenset(range(self.adj.shape[0]))
        self.tree = self.construct_contractiontree(order)
        self.seed = seed
        self.rng = np.random.RandomState(seed)
        self.slicing_edges = []

    def construct_contractiontree(self, order):
        self.order = order
        tree = []
        current_branch = {}
        for edge in order:
            m, n = edge
            if m not in current_branch.keys():
                left = ContractionVertex(frozenset([m]), None, None, None)
                tree.append(left)
            else:
                left = current_branch[m]
            if n not in current_branch.keys():
                right = ContractionVertex(frozenset([n]), None, None, None)
                tree.append(right)
            else:
                right = current_branch[n]
            parent = ContractionVertex(left.contain_nodes | right.contain_nodes, None, left, right)
            tree.append(parent)
            current_branch[m] = parent
            left.parent = parent
            right.parent = parent
        return tree
    
    def slicing(self, edges):
        if type(edges) is tuple:
            edges = [edges]
        for edge in edges:
            i, j = edge
            assert edge in self.edges
            idxi_j = self.neighbors[i].index(j)
            idxj_i = self.neighbors[j].index(i)
            self.neighbors[i].pop(idxi_j)
            self.neighbors[j].pop(idxj_i)
            self.shapes[i].pop(idxi_j)
            self.shapes[j].pop(idxj_i)
            self.edges.remove(edge)
            self.adj[i, j] = 0
            self.adj[j, i] = 0
            self.slicing_edges.append(edge)
        self.slicing_edges.sort()
    
    def check_contractiontree(self):
        root = self.tree[-1]
        self.tree = [root]
        current_vertices = [root]
        while current_vertices:
            next_vertices = []
            for vertex in current_vertices:
                if vertex.left and vertex.right:
                    next_vertices += [vertex.left, vertex.right]
                    self.tree += [vertex.left, vertex.right]
            current_vertices = next_vertices
        self.tree.reverse()

    def tree_to_tn(self, tree_leaves):
        nodes_outof_tree = deepcopy(self.all_nodes)
        for i in range(len(tree_leaves)):
            nodes_outof_tree -= tree_leaves[i].contain_nodes
        neighbors, shapes = [[] for i in range(len(tree_leaves) + 1)], [[] for i in range(len(tree_leaves) + 1)]
        for i in range(len(tree_leaves)):
            nodes_i = tree_leaves[i].contain_nodes
            for j in range(i+1, len(tree_leaves)+1):
                if j != len(tree_leaves):
                    nodes_j = tree_leaves[j].contain_nodes
                else:
                    nodes_j = nodes_outof_tree
                log_cutsize_ij = cut_size(self.adj, list(nodes_i), list(nodes_j))
                cutsize_ij = 2 ** log_cutsize_ij
                if log_cutsize_ij != 0:
                    neighbors[i].append(j)
                    neighbors[j].append(i)
                    shapes[i].append(cutsize_ij)
                    shapes[j].append(cutsize_ij)
        # for i in range(len(neighbors)):
        #     print(i, neighbors[i], shapes[i])

        return Contraction(None, neighbors, shapes)
    
    def tree_to_order(self):
        tree = self.tree
        current_vertices = [tree[-1]]
        order = []
        while current_vertices:
            next_vertices = []
            for vertex in current_vertices:
                if vertex.left and vertex.right:
                    next_vertices += [vertex.left, vertex.right]
                    rep_nodes = [min(vertex.left.contain_nodes), min(vertex.right.contain_nodes)]
                    order.append((min(rep_nodes), max(rep_nodes)))
            current_vertices = next_vertices
        order.reverse()
        return order
    
    # just for test
    def localtree2order(self, root, tree_leaves):
        order = []
        current_leaves = list(tree_leaves)
        tree_leaves_contain_nodes = [vertex.contain_nodes for vertex in tree_leaves]
        i = 0
        while current_leaves[0].contain_nodes != root.contain_nodes:
            for j in range(i+1, len(current_leaves)):
                if current_leaves[i].parent.contain_nodes == current_leaves[j].parent.contain_nodes:
                    order.append((i, j))
                    current_leaves.append(current_leaves[i].parent)
                    tree_leaves_contain_nodes.append(current_leaves[-1].contain_nodes)
                    current_leaves.pop(j)
                    tree_leaves_contain_nodes.pop(j)
                    current_leaves.pop(i)
                    tree_leaves_contain_nodes.pop(i)
                    i = 0
                    break
                if j == len(current_leaves) - 1:
                    i += 1
        return order
    
    def spanning_tree(self, root, size=8):
        stack = [root]
        leaves = []
        tree_vertices = []

        while len(stack) + len(leaves) < size and len(stack):
            vertex = stack.pop(0)
            tree_vertices.append(vertex)

            if len(vertex.contain_nodes) == 1:
                leaves.append(vertex)
            else:
                stack.append(vertex.left)
                stack.append(vertex.right)

        tree_leaves = stack + leaves
        tree_vertices += stack
        tree_vertices.reverse()

        return tree_leaves, tree_vertices
    
    def local_search(self, size, steps=100):
        initial_score, initial_tc, initial_sc = self.tree_complexity()
        for step in range(steps):
            sub_root = self.rng.choice(self.tree)
            local_tree_leaves, local_tree = self.spanning_tree(sub_root, size)
            # print([sorted(list(local_tree_leave.contain_nodes)) for local_tree_leave in local_tree_leaves])
            if len(local_tree_leaves) <= 2:
                continue
            reference_score, tc_tree, sc_tree = self.tree_complexity(local_tree, sub_root)
            if sc_tree <= initial_sc:
                reference_score = tc_tree
            tn_local_tree = self.tree_to_tn(local_tree_leaves)
            # order_sub = ctg2normal(self.localtree2order(sub_root, local_tree_leaves))
            # print(order_sub)
            # tc_tn, sc_tn = tn_local_tree.contraction_partorder(order_sub)[:2]
            # if abs(tc_tn - tc_tree) > 1e-6 or abs(sc_tn - sc_tree) > 1e-6:
            #     print(tc_tn, tc_tree, sc_tn, sc_tree)
            # assert abs(tc_tn - tc_tree) < 1e-6 and abs(sc_tn - sc_tree) < 1e-6
            com = [i for i in range(len(local_tree_leaves))]
            results = []
            for i in range(20):
                tcs, scs, order_new = tn_local_tree.contraction_one_community(com, strategy='max_reduce', seed=i)
                if len(order_new) != len(com) - 1:
                    print(order_new, com)
                assert len(order_new) == len(com) - 1
                tc, sc = log10sumexp2(tcs), max(scs)
                if sc <= initial_sc:
                    score = tc
                else:
                    score = score_fn(tc, sc)
                # print(i, tc, sc, score)
                results.append((score, order_new, tc, sc))
            score_new, order_new = sorted(results, key=lambda r:r[0])[0][:2]
            # print(score_new, reference_score)
            if score_new < reference_score:
                original_score, original_tc, original_sc = self.tree_complexity()
                self.apply_order(order_new, local_tree_leaves, sub_root)
                self.check_contractiontree()
                after_score, after_tc, after_sc = self.tree_complexity()
                if after_score > original_score:
                    print('-'*20)
                    print(original_score, original_tc, original_sc)
                    print(after_score, after_tc, after_sc)
                    print(score_new, reference_score)
                    # print(results[0][2:], tc_tn, sc_tn)
                    print('-'*20)
                # assert after_score <= original_score
                # order1 = self.tree_to_order()
                # r = model.contraction_partorder(order1)
                # print('tn contraction result:', r[:2], score_fn(r[0], r[1]))
                # self.tree_complexity()
        
        return self.tree_to_order()
    
    def apply_order(self, order, tree_leaves, root):
        for i, j in order:
            left, right = tree_leaves[i], tree_leaves[j]
            if (i, j) != order[-1]:
                parent = ContractionVertex(left.contain_nodes | right.contain_nodes, None, left, right)
            else:
                try:
                    assert left.contain_nodes | right.contain_nodes == root.contain_nodes
                except:
                    print(root.contain_nodes)
                    print(i, j, order, len(tree_leaves))
                    for leave in tree_leaves:
                        print(leave.contain_nodes)
                    print_exc()
                    sys.exit(0)
                parent = root
                root.left = left
                root.right = right
            left.parent = parent
            right.parent = parent
            tree_leaves[i] = parent
    
    def tree_complexity(self, tree=None, root=None):
        if tree is None:
            tree = self.tree
        if root is None:
            root = tree[-1]
        assert root == tree[-1]
        current_vertices = [tree[-1]]
        tcs, sc = [], 0
        while current_vertices:
            next_vertices = []
            for vertex in current_vertices:
                left, right = vertex.left, vertex.right
                if left and right and left in tree and right in tree:
                    # tree.remove(left)
                    # tree.remove(right)
                    next_vertices += [left, right]
                    vertex_sc = cut_size(self.adj, list(vertex.contain_nodes))
                    logshape_l_r = cut_size(self.adj, list(left.contain_nodes), list(right.contain_nodes))
                    logshape_l = cut_size(self.adj, list(left.contain_nodes)) - logshape_l_r
                    logshape_r = cut_size(self.adj, list(right.contain_nodes)) - logshape_l_r
                    # print(vertex_sc, logshape_l, logshape_l_r, logshape_r, '1234')
                    sc = max([sc, vertex_sc, logshape_l + logshape_l_r, logshape_r + logshape_l_r])
                    tcs.append(logshape_l + logshape_l_r + logshape_r)
            current_vertices = next_vertices
        tc = log10sumexp2(tcs)
        score = score_fn(tc, sc)
        # print('contraction tree result:', tc, sc, score)
        return score, tc, sc

    def order_merge(self):
        return
    
    def copy(self):
        ctree = ContractionTree(deepcopy(self.neighbors), deepcopy(self.shapes), deepcopy(self.order), deepcopy(self.edges), self.seed)
        return ctree

def dynamic_slicing(model, group_slicing, order, gpu_memory_limit=30, seed_order=0, first_local=False, random_init=True):
    """
    Dynamic slicing function for finding slicing edges and associated order

    Input:
    ======
    model: Class, given tensor network class
    group_slicing: list of tensor ids, group of tensors need to be sliced
    order: list of tuples, initial order
    gpu_memory_limit: Int, largest intermediate tensors that can be stored in the GPU, 30 for 32G
    seed_order: Int, seed for the dynamic slicing process

    Output:
    =======
    order_final: list of tuples, resulting sliced order
    slicing_edges_final: list of tuples, resulting slicing edges
    
    """
    sys.setrecursionlimit(2000)

    order = [(i, j) for i, j in order if i in group_slicing and j in group_slicing]
    rng = np.random.RandomState(seed_order)
    neighbors, shapes = model.neighbors, model.shapes
    edges = []
    for i in range(len(neighbors)):
        for j in range(len(neighbors[i])):
            if i < neighbors[i][j]:
                edges.append((i, neighbors[i][j], log2(2.0)))
    
    edges_pool = [(edge[0], edge[1]) for edge in edges if edge[0] in group_slicing or edge[1] in group_slicing]
    ctree = ContractionTree(neighbors, shapes, order, edges_pool, seed_order)

    result1 = model.contraction_partorder(order)
    print('original result:', result1[:2], score_fn(result1[0], result1[1]))

    if first_local:
        order_new = ctree.local_search(12, 500)
        result2 = slicing_partorder_complexity(neighbors, shapes, order_new)
        print('after local search:', result2[:2], score_fn(result2[0], result2[1]))
    else:
        order_new = order

    num_keep, num_trees = 4, 2
    
    tc, sc, _, _ = slicing_partorder_complexity(neighbors, shapes, order_new)
    score = score_fn(tc, sc)
    if sc <= gpu_memory_limit:
        print('after slice 0 edges, tc {} sc {} score {}, sliced tc {}'.format(tc, sc, score, tc))
        return order_new, []

    tns_current = [ctree]
    results_all = []    
    while True:
        for tn in tns_current:
            info_after = []
            score1, tc1, sc1 = tn.tree_complexity()
            print('before:', tc1, sc1, score1)
            # if len(edges_sliced):
            #     edge = edges_sliced.pop(0)
            #     tc_tmp, sc_tmp, _, _ = slicing_partorder_complexity(tn.neighbors, tn.shapes, tn.order, edge)
            #     info_after.append((edge, score_fn(tc_tmp, sc_tmp)))
            # else:
            for edge in tn.edges:
                tc_tmp, sc_tmp, _, _ = slicing_partorder_complexity(tn.neighbors, tn.shapes, tn.order, edge)
                info_after.append((edge, score_fn(tc_tmp, sc_tmp)))
            
            if random_init:
                if len(tn.slicing_edges) == 0:
                    indices = rng.choice(len(info_after), num_keep)
                    # indices = rng.choice(np.arange(len(info_after)), num_keep, replace=False)
                    candidates = [info_after[idx] for idx in indices]
                elif len(tn.slicing_edges) == 1:
                    indices = rng.choice(len(info_after), num_trees)
                    # indices = rng.choice(np.arange(len(info_after)), num_trees, replace=False)
                    candidates = [info_after[idx] for idx in indices]
                else:
                    candidates = sorted(info_after, key=lambda info:info[1])[:num_trees]
            else:
                if len(tn.slicing_edges) == 0:
                    candidates = sorted(info_after, key=lambda info:info[1])[:num_keep]
                else:
                    candidates = sorted(info_after, key=lambda info:info[1])[:num_trees]

            tns_tmp = [deepcopy(tn) for i in range(len(candidates))]
            for i in range(len(candidates)):
                assert len(tns_tmp[i].slicing_edges) + len(tns_tmp[i].edges) == len(edges_pool)
            for i in range(len(candidates)):
                edge = candidates[i][0]
                tns_tmp[i].slicing(edge)

                # kickoff result
                new_order1, scs1, tcs1, _, _ = kickoff_group(group_slicing.copy(), tns_tmp[i], seed=seed_order, n_trials=30) # completely new order result
                tc1, sc1, _, _ = slicing_partorder_complexity(tns_tmp[i].neighbors, tns_tmp[i].shapes, new_order1)
                score1 = score_fn(tc1, sc1)
                
                # local search result
                new_order0 = tns_tmp[i].local_search(12, 500) 
                score0, tc0, sc0 = tns_tmp[i].tree_complexity()

                print(f"new order 0 tc {tc0} sc {sc0}")
                print(f"new order 1 tc {tc1} sc {sc1}")

                idx = int(score0 > score1)
                new_order = [new_order0, new_order1][idx] # new_order0 # 
                assert len(new_order) == len(group_slicing) - 1
                tns_tmp[i].tree = tns_tmp[i].construct_contractiontree(new_order)
                new_result = {
                    'tc': [tc0, tc1][idx], # tc0, #
                    'sc': [sc0, sc1][idx], # sc0, # 
                    'score' : [score0, score1][idx], # score0, #  
                }
                results_all.append({'tn': tns_tmp[i], **new_result})
                print(results_all[-1]['tc'], results_all[-1]['sc'], results_all[-1]['score'])
        results_all.sort(key=lambda x:x['score'])
        indices = [0]
        for i in range(1, len(results_all)):
            equal_flag = False
            for j in indices:
                if results_all[i]['tn'].slicing_edges == results_all[j]['tn'].slicing_edges:
                    equal_flag = True
                    break
            if not equal_flag:
                indices.append(i)
        results_all = [results_all[i] for i in indices[:num_keep]]
        tns_current = [result['tn'] for result in results_all]
        for result in results_all:
            tn, tc, sc, score = result['tn'], result['tc'], result['sc'], result['score']
            print(results_all.index(result), len(tn.slicing_edges), tn.slicing_edges, tc, sc, score)
            if sc <= gpu_memory_limit:
                print('after slice {} edges, tc {} sc {} score {}, sliced tc {}'.format(len(tn.slicing_edges), tc, sc, score, log10(2**len(tn.slicing_edges)) + tc))
                order_final, slicing_edges_final = tn.order, tn.slicing_edges
                return order_final, slicing_edges_final

if __name__ == "__main__":
    from .args import args

    n, m, seed, seed2, simplify, seq = args.n, args.m, args.seed, args.seed2, args.simplify, args.seq
    
    # tensors, labels = get_data(n, m, seed, simplify, args.seq)
    tensors, labels, final_qubits_representation = get_tensors(n, m, seq=seq, simplify=simplify)
    
    model = Contraction(tensors, labels)
    
#     sc_target, tc_single_step_target = args.sc, args.tc
#     # sc_target, tc_single_step_target = 39, 42
#     # sc_target, tc_single_step_target = 36, 39
#     # sc_target, tc_single_step_target = 31, 40
#     # sc_target, tc_single_step_target = 34, 37
#     # sc_target, tc_single_step_target = 52, 56

#     t0 = time.time()
#     if args.method == 'bipartition':
#         results = model.bipartition(sc_target, tc_single_step_target, seed=args.seed2)
#     elif args.method == 'kickoff':
#         results = model.order_kickoff(sc_target, tc_single_step_target, seed=args.seed2, n_trials=args.trials)
#     else:
#         raise ValueError("Specify an method using -method [bipartition, kickoff, kickoff3]")
#     print('time of finding order:', time.time() - t0)
#     print(results[0], len(results[0]))
    
#     if results is not None:
#         # write_order(results[0], 'sycamore_newcut/order/EFGH/bipartition_n{}m{}seed{}Dmax70000000cutoff0.0simplify.txt'.format(n, m, seed))
#         # write_community(results[1], 'sycamore_newcut/order/EFGH/bipartition_n{}m{}seed{}Dmax70000000cutoff0.0simplify_group.txt'.format(n, m, seed))
#         tc, sc, tcs, scs, _ = model.contraction(order=results[0].copy())
#         print("Order found, tc: {:.5f}, sc: {:.1f}".format(tc, sc))
#         print("tc of each steps: ", tcs)
#         print("sc of each steps: ", scs)
#         # _, _, _, _, slice_list = contraction_slicing_new1(model.shapes, model.neighbors, results[0], args.gpu_limit)
#         # print('slicing edges: ', slice_list)
#     else:
#         print("Desired order not found.")
    
#     part_top = results[2]
#     final_qubits_num = [[], []]
#     for i in range(2):
#         for node in part_top[i]:
#             if node in final_qubits_representation.keys():
#                 final_qubits_num[i] += final_qubits_representation[node]
#     print(final_qubits_representation)
#     print('initial partition:', part_top)
#     print('qubits of each partition', final_qubits_num)
#     print('qubits num', (len(final_qubits_num[0]), len(final_qubits_num[1])))
#     print('cut size of initial partition', results[3])


#     bipartition_order_filename = join(dirname(__file__), 'slicing_order/bipartition_n{}_m{}_s{}_{}_s2{}_{}.txt'.format(
#         n, m, seed, seq, seed2, 'simplify_' if simplify else '' 
#     ))
#     # write_community(part_top, bipartition_order_filename)
# '''
#     if min(final_qubits_num) > 10:
#         write_community(part_top, bipartition_order_filename)
#         for trial in range(20):
#             dynamic_slicing(tc+0.5, sc+1, n, m, seed, seq, simplify, args.gpu_limit, seed2=trial)
# '''
    import cotengra as ctg

    # eq, sizes, _, _ = model._labels_to_einsum(group_slicing)
    # opt = ctg.HyperOptimizer(methods=['kahypar'], parallel='ray')
    # path, info_initial = oe.contract_path(eq, *sizes, shapes=True, optimize=opt)
    # order = [(group_slicing[i], group_slicing[j]) for i, j in ctg2normal(path)]

    # tree = ctg.ContractionTree.from_info(info_initial)
    # tree_sf = tree.slice_and_reconfigure_forest(
    #     parallel='ray',
    #     target_size=2**30,
    #     num_trees=4,
    #     reconf_opts={
    #         'subtree_size': 12,
    #         'forested': True,
    #         'num_trees': 4,
    #     }
    # )
    # print(f'{len(tree_sf.sliced_inds)} slicing complexity {log10(tree_sf.total_flops()/2)} {log10(tree_sf.total_flops()/2**(len(tree_sf.sliced_inds)+1))}')

    gpu_memory_limit = 30
    # order_rep = read_order(f'bighead/slicing_order/n{n}_m{m}_s{seed}_{seq}_s2{seed2}_simplify_gpulimit_{gpu_memory_limit}_ordernew.txt')
    order_rep, _, _, _ = model.bipartition(53, 57, 4)
    group = read_community(f'bighead/slicing_order/bipartition_n{n}_m{m}_s{seed}_{seq}_s2{seed2}_simplify_.txt')
    slicing_idx = 0 if len(group[0]) > len(group[1]) else 1
    group_slicing = group[slicing_idx]

    order_new, slicing_edges = dynamic_slicing(model, group_slicing, order_rep, seed_order=args.seed_mcmc)