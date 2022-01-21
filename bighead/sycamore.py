from .loadtensor import get_tensors
from .utils import *
from .order import Contraction
import numpy as np
from numpy import binary_repr
from os.path import join, dirname, exists
import time
from copy import deepcopy
from sys import exit
from math import log10, log2, sqrt
from .args import args
from traceback import print_exc

'''
commandline example:
python3 -m BiparitionBatch.sycamore -seed2 4 -simplify -task_start 0 -task_end 4096  # slicing subtask calculation
python3 -m BiparitionBatch.sycamore -seed2 4 -simplify -task_start 0 -task_end 64 -sampling_method all  # calculate all samples probability
python3 -m BiparitionBatch.sycamore -seed2 4 -simplify -task_start 0 -task_end 64 -sampling_method mcmc  # MCMC samping and calculation samples probability
'''

def find_community_order_rearrange(order, group):
    '''
    function for finding communtiy and rearrange order of given order,
    result in an order with small time(space) complexity on the front

    Input:
    ======
    order: given order, supposed to be part of entire order
    group: overall groups of nodes in order

    Output:
    =======
    community_dict: dictionary of communities
    L: length of orders being moved to the front
    order_new: rearranged orders
    '''
    if type(group) is int:
        group = range(group)
    
    order_rearrange_idx = []

    community_dict = {i:[i] for i in group}
    for i in range(len(order)):
        m, n = order[i]
        community_dict[m] += community_dict[n]
        community_dict.pop(n)
        if len(community_dict[m]) <= 40: # conditions to determine whether this step should be rearanged
            order_rearrange_idx.append(i)
    order_tmp = deepcopy(order)
    order_new = []
    for idx in order_rearrange_idx:
        order_new.append(order[idx])
        order_tmp.remove(order[idx])
    for edge in order_tmp:
        order_new.append(edge)

    L = len(order_rearrange_idx)
    assert len(order_new) == len(order)
    
    return community_dict, L, order_new


def order_merge(order, eq_sep):
    '''
    function for merging branch, indicate to increase GPU efficiency
    
    Input:
    ======
    order: given order
    eq_sep: list of equations represent the tensor network

    Output:
    =======
    order_new: order after merging small branch
    '''
    eq = deepcopy(eq_sep)
    order_new = deepcopy(order)
    edge_rearrange_idx = []
    for edge in order:
        i, j = edge
        tmp = eq[i] + eq[j]
        common = frozenset(eq[i]) & frozenset(eq[j])
        idx_remove = []
        for n in range(len(tmp)):
            if tmp[n] in common:
                idx_remove.insert(0, n)
        for idx in idx_remove:
            tmp = tmp[:idx] + tmp[idx+1:]
        shapeij = len(idx_remove) / 2
        li = len(eq[i])
        shapei = li - shapeij
        lj = len(eq[j])
        shapej = lj - shapeij
        tc = shapei+shapeij+shapej+1
        min_node = i if shapei < shapej else j
        # print(shapei+shapeij+shapej+1, li, lj, shapeij)
        
        if tc >= 25 and shapeij < 5 and min(shapei, shapej) < 5: # conditions to determine whether this branch should be merged
            edge_rearrange_idx.append((order.index(edge), min_node))
        
        eq[i] = tmp
        eq[j] = []
    
    while len(edge_rearrange_idx) > 0:
        # pop 3 three steps every time, and merge the first two branch into one big branch
        data = edge_rearrange_idx[:3]
        indices = []
        min_nodes = []
        for idx, min_node in data:
            min_nodes.append(min_node)
            indices.append(idx)
        if len(indices) == 3 and indices[1] - indices[0] == indices[2] - indices[1] == 1: # determine whether three steps are continuous
            i, j = order_new[indices[0]]
            stem_node = i if j == min_nodes[0] else j
            if order_new[indices[2]][0] == stem_node:
                order_new[indices[0]] = (min_nodes[1], min_nodes[0])
                order_new[indices[1]] = (min_nodes[2], min_nodes[1])
                order_new[indices[2]] = (stem_node, min_nodes[2])
            elif order_new[indices[2]][0] == min_nodes[0]:
                order_new[indices[0]] = (min_nodes[0], min_nodes[1])
                order_new[indices[1]] = (min_nodes[0], min_nodes[2])
                order_new[indices[2]] = (min_nodes[0], stem_node)
            elif order_new[indices[2]][0] == min_nodes[1]:
                order_new[indices[0]] = (min_nodes[1], min_nodes[0])
                order_new[indices[1]] = (min_nodes[1], min_nodes[2])
                order_new[indices[2]] = (min_nodes[1], stem_node)
            elif order_new[indices[2]][0] == min_nodes[2]:
                order_new[indices[0]] = (min_nodes[2], min_nodes[0])
                order_new[indices[1]] = (min_nodes[2], min_nodes[1])
                order_new[indices[2]] = (min_nodes[2], stem_node)
        for d in data:
            edge_rearrange_idx.remove(d)
    
    return order_new

def fix_bitstring(bitstring, qubits_position, bitstring_mcmc):
    '''
    function for change qubit data in bitstrings at certain positions

    Input:
    ======
    bitstring: original bitstring
    qubits_position: qubits position need to change
    bitstring_mcmc: bistring of qubit position to replace

    Output:
    =======
    fixed bitstring
    '''
    string_list = list(bitstring)
    for i in range(len(qubits_position)):
        string_list[qubits_position[i]] = bitstring_mcmc[i]
    return ''.join(string_list)

def flip(bitstring, rng, qubits_position=None):
    '''
    flip bitstring in one qubit at given qubits position

    Input:
    ======
    bitstring: original bitstring
    rng: a numpy.random.Randomstate, used to generate flip position
    qubits_position: qubits position

    Output:
    =======
    next_bitstring: flipped bitstring
    '''
    if qubits_position is None:
        idx = rng.choice(len(bitstring))
    else:
        idx = rng.choice(qubits_position)
    next_bitstring = list(bitstring)
    if next_bitstring[idx] == '0':
        next_bitstring[idx] = '1'
    else:
        next_bitstring[idx] = '0'
    next_bitstring = ''.join(next_bitstring)

    return next_bitstring

def contraction_scheme(eq_sep, order):
    '''
    construct a scheme by given order

    Input:
    ======
    eq_sep: list of equations represent the tensor network
    order: given order

    Output:
    =======
    contraction scheme: constructed contraction scheme
    eq_sep[i]: equation of final tensor
    '''
    contraction_scheme = []

    for edge in order:
        i, j = edge
        ei, ej = eq_sep[i], eq_sep[j]
        common_indices = sorted(frozenset(ei) & frozenset(ej))
        if len(common_indices) == 0:
            flag = False
        else:
            flag = True
        if flag:
            idxi_j = []
            idxj_i = []
            for idx in common_indices:
                idxi_j.append(ei.index(idx))
                idxj_i.append(ej.index(idx))
            eq_sep[i] = ''.join([ei[m] for m in range(len(ei)) if m not in idxi_j] + [ej[n] for n in range(len(ej)) if n not in idxj_i])
            contraction_scheme.append((edge, 'tensordot', idxi_j, idxj_i))
        else:
            eq_sep[i] = ei + ej
            contraction_scheme.append((edge, 'outer'))
    
    return contraction_scheme, eq_sep[i]

def tensor_contraction(tensors, contraction_scheme, get_time=False):
    '''
    tensor contraction by given contraction scheme

    Input:
    ======
    tensors: list of tensors to be contracted
    contraction_scheme: list of contraction schemes, in the format of (tensor position i, tensor position j, tensordot or outer, tensordot indices param if tensordot)
    get_time: return gpu time or not

    Output:
    =======
    tc: overall time complexity of contraction
    time_complexity: tc of each step
    sc: overall space complexity of contraction
    space_complexity: sc of each step
    time_spend: if get_time parameter is True, return a list of gpu time of each step, else return an empty list
    tensors[i]: return the resulting tensor after contraction
    '''
    time_complexity = []
    space_complexity = [max([log2(prod(tensors[i].shape)) for i in range(len(tensors)) if not isinstance(tensors[i], list)])]
    time_spend = []
    for step in contraction_scheme:
        i, j = step[0]
        try:
            shapei, shapej = prod(tensors[i].shape), prod(tensors[j].shape)
        except:
            print_exc()
            print(step, i, j, tensors[i], tensors[j])
            exit(1)
        if get_time:
            torch.cuda.synchronize()
            t_start = time.time()
        if step[1] == 'tensordot':
            try:
                tensors[i] = torch.tensordot(tensors[i], tensors[j], (step[2], step[3]))
            except Exception as identifier:
                print(i, j, tensors[i].shape, tensors[j].shape, log2(shapei), log2(shapej), step[2], step[3])
                print(identifier)
                exit(1)
        elif step[1] == 'outer':
            tensors[i] = torch.outer(tensors[i].reshape(-1), tensors[j].reshape(-1)).reshape(tensors[i].shape + tensors[j].shape)
        else:
            print(step)
            raise ValueError('Wrong contraction scheme!')
        if get_time:
            torch.cuda.synchronize()
            t_end = time.time()
            time_spend.append(t_end - t_start)
        shapeij = prod(tensors[i].shape)
        time_complexity.append(log2(sqrt(shapei*shapej*shapeij)))
        space_complexity.append(max(space_complexity[-1], log2(shapeij)))
        tensors[j] = []
    tc = log10sumexp2(time_complexity)
    sc = max(space_complexity)
    return tc, time_complexity, sc, space_complexity, time_spend, tensors[i]


class SycamoreBipartitionBatch:
    def __init__(self, n, m, seed, seq, seed2, simplify, gpu_limit, cuda, seed_mcmc,
                 complex128=False, sampling_method='all', burn_in=10, num_samples=20, num_chains=25, **kwargs):
        self.n, self.m, self.seed, self.seq, self.seed2, self.simplify, self.gpu_limit, self.complex128, self.seed_mcmc, self.sampling_method =\
             n, m, seed, seq, seed2, simplify, gpu_limit, complex128, seed_mcmc, sampling_method
        self.burn_in, self.num_samples, self.num_chains = burn_in, num_samples, num_chains
        self.rng = np.random.RandomState(0)
        self.device = 'cuda:{}'.format(cuda) if cuda >= 0 else 'cpu'
        self.dtype = torch.complex128 if complex128 else torch.complex64
        self.bitstring = binary_repr(seed_mcmc, n) # '0' * n # binary_repr(self.rng.randint(2**n), n)

        openqubits_filename = join(dirname(__file__), 'slicing_order/openqubits_n{}_m{}_s{}_{}_s2{}_{}.txt'.format(
            n, m, seed, seq, seed2, 'simplify_' if simplify else '' 
        ))
        if exists(openqubits_filename):
            self.open_qubits = read_community(openqubits_filename)
        else:
            self.open_qubits = None
        self.tensors, self.labels, final_qubit_represent, self.qubits_representation, self.remain_nodes, self.simplify_order = \
             get_tensors(n, m, seed, seq=seq, bitstring=self.bitstring, simplify=simplify, get_details=True, open_qubits=self.open_qubits)
        '''
        self.tensors_torch = []
        for i in range(len(self.labels)):
            self.tensors_torch.append(torch.from_numpy(self.tensors[i]).to(self.dtype).to(self.device))
        '''
        self.model = Contraction(self.tensors, self.labels)
        self.eq, _, _, _ = self.model._labels_to_einsum()
        self.eq_sep = self.eq.split('->')[0].split(',')
        group_filename = join(dirname(__file__), 'slicing_order/bipartition_n{}_m{}_s{}_{}_s2{}_{}.txt'.format(
            n, m, seed, seq, seed2, 'simplify_' if simplify else '' 
        ))
        sliced_edges_filename = join(dirname(__file__), 'slicing_order/n{}_m{}_s{}_{}_s2{}_{}gpulimit_{}_edges.txt'.format(
            n, m, seed, seq, seed2, 'simplify_' if simplify else '', gpu_limit
        ))
        sliced_order_filename = join(dirname(__file__), 'slicing_order/n{}_m{}_s{}_{}_s2{}_{}gpulimit_{}_ordernew.txt'.format(
            n, m, seed, seq, seed2, 'simplify_' if simplify else '', gpu_limit
        ))
        self.data_filename = join(dirname(__file__), 'samples/n{}_m{}_s{}_{}_s2{}_sm{}_{}gpulimit_{}_data{}.pt'.format(
            n, m, seed, seq, seed2, seed_mcmc, 'simplify_' if simplify else '', gpu_limit, '_complex128' if complex128 else '_complex64'
        ))
        self.samples_filename = join(dirname(__file__), 'samples/n{}_m{}_s{}_{}_s2{}_sm{}_{}gpulimit_{}_samples{}.txt'.format(
            n, m, seed, seq, seed2, seed_mcmc, 'simplify_' if simplify else '', gpu_limit, '_complex128' if complex128 else '_complex64'
        ))
        self.mcmc_filename = join(dirname(__file__), 'samples/n{}_m{}_s{}_{}_s2{}_sm{}_{}gpulimit_{}_mcmc{}.txt'.format(
            n, m, seed, seq, seed2, seed_mcmc, 'simplify_' if simplify else '', gpu_limit, '_complex128' if complex128 else '_complex64'
        ))

        group = read_community(group_filename)
        slicing_idx = 0 if len(group[0]) > len(group[1]) else 1
        self.group_slicing = group[slicing_idx]
        self.group_mcmc = group[(slicing_idx+1)%2]
        final_qubits_part = [[], []]
        for i in range(len(group)):
            for j in group[i]:
                if j in final_qubit_represent.keys():
                    final_qubits_part[i] += final_qubit_represent[j]

        min_qubit_idx = min(min(final_qubits_part[0]), min(final_qubits_part[1]))
        for i in range(2):
            final_qubits_part[i] = [item - min_qubit_idx for item in final_qubits_part[i]]
        self.final_qubits_mcmc = final_qubits_part[(slicing_idx+1)%2]
        self.final_qubits_slicing = final_qubits_part[slicing_idx]

        self.order_slicing = read_order(sliced_order_filename)
        self.sliced_edges = read_order(sliced_edges_filename)

    def batch_sampling(self):
        if exists(self.data_filename):
            tensor_slicing, eq_slicing = torch.load(self.data_filename)
        else:
            raise ValueError('Slicing data not found')
        tensors, labels, _ = get_tensors(self.n, self.m, self.seed, seq=self.seq, bitstring=self.bitstring, simplify=False)
        l_tensors = len(tensors)
        group_sampling = []
        for node in self.group_mcmc:
            group_sampling += self.qubits_representation[self.remain_nodes[node]]
        
        tensors_torch = []
        labels_sampling = []
        for i in group_sampling:
            tensors_torch.append(torch.from_numpy(tensors[i]).to(tensor_slicing.dtype).to(self.device))
        
        final_qubits = list(range(len(labels) - self.n, len(labels)))
        closed_group = []
        qubits_sampling = []
        slicing_opposite_indices = []
        for i in range(len(group_sampling)):
            neighbor = labels[group_sampling[i]]
            tmp = []
            for node in neighbor:
                if node in group_sampling:
                    tmp.append(group_sampling.index(node))
                else:
                    tmp.append(len(group_sampling)) # point to tensor_slicing, which will be put into the end of tensors_torch
                    slicing_opposite_indices.append((i, node))
            assert len(tmp) == len(neighbor)
            labels_sampling.append(tmp)
            if group_sampling[i] in final_qubits:
                qubits_sampling.append(group_sampling[i])
            else:
                closed_group.append(i)
        qubits_sampling.sort()
        label_slicing = []
        for symbol in eq_slicing:
            edge = self.model.edges[char2idx(symbol)]
            if edge[0] in self.group_slicing:
                slicing_node, target_node = edge[0], edge[1]
            elif edge[1] in self.group_slicing:
                slicing_node, target_node = edge[1], edge[0]
            else:
                raise ValueError('Error occurs in equation slicing')
            for idx, node in slicing_opposite_indices:
                if node in self.qubits_representation[self.remain_nodes[slicing_node]] and group_sampling[idx] in self.qubits_representation[self.remain_nodes[target_node]]:
                    label_slicing.append(idx)
        assert len(label_slicing) == len(eq_slicing)
        labels_sampling.append(label_slicing)
        tensors_torch.append(tensor_slicing.to(self.device))
        assert len(labels_sampling) == len(tensors_torch)
        closed_group.append(len(labels_sampling) - 1)

        model_sampling = Contraction(tensors_torch, labels_sampling)
        tc, sc, order_sampling = model_sampling.contraction_one_community(closed_group, strategy='max_reduce_tri', seed=self.seed_mcmc)

        eq, _, _, _ = model_sampling._labels_to_einsum()
        eq_sep = eq.split('->')[0].split(',')
        scheme, eq_sampling = contraction_scheme(eq_sep, order_sampling)
        assert len(eq_sampling) == len(qubits_sampling)

        tc, tcs, sc, scs, time_spend, tensor_sampling = tensor_contraction(tensors_torch, scheme)

        idx_open_qubits = np.empty(len(eq_sampling), dtype=np.int)
        for i in range(len(eq_sampling)):
            edge = model_sampling.edges[char2idx(eq_sampling[i])]
            if group_sampling[edge[0]] in qubits_sampling:
                idx_open_qubits[qubits_sampling.index(group_sampling[edge[0]])] = i
            elif group_sampling[edge[1]] in qubits_sampling:
                idx_open_qubits[qubits_sampling.index(group_sampling[edge[1]])] = i
            else:
                raise ValueError('Error occurs in small head contraction!')
            
        tensor_sampling = tensor_sampling.permute(tuple(idx_open_qubits)).reshape(-1)
        amplitude = tensor_sampling.cpu().numpy().reshape(-1)
        batch_prob = np.linalg.norm(amplitude.reshape(1, -1), axis=0) ** 2
        # print(2**53 * batch_prob.mean() - 1, len(batch_prob), batch_prob[:32])
        samples_data = []
        l = len(self.final_qubits_mcmc)
        self.final_qubits_mcmc.sort()
        for qubit, location in zip(self.final_qubits_mcmc, qubits_sampling):
            assert location - qubit == l_tensors - self.n
        for i in range(2**l):
            bitstring_sampling = binary_repr(i, l)
            current_bitstring = fix_bitstring(deepcopy(self.bitstring), self.final_qubits_mcmc, bitstring_sampling)
            samples_data.append((current_bitstring, batch_prob[i], amplitude[i]))
        write_samples(samples_data, self.samples_filename)

        return samples_data, amplitude
    
    def slicing_subtasks(self, segment, task_num=11):
        '''
        employ subtasks for contraction of slicing group, 
        each one will calculate 2**task_num subtasks and add all resulting tensors together and store it.
        '''
        data_filename = join(dirname(__file__), 'slicing_components/n{}_m{}_s{}_{}_s2{}_sm{}_{}gpulimit_{}_data{}_{}.pt'.format(
            self.n, self.m, self.seed, self.seq, self.seed2, self.seed_mcmc, 'simplify_' if self.simplify else '', 
            self.gpu_limit, '_complex128' if self.complex128 else '_complex64', segment
        ))
        torch.cuda.synchronize(self.device)
        t_start = time.time()
        t_calculation = 0

        group_dict, l, order_rep = find_community_order_rearrange(self.order_slicing, range(len(self.group_slicing)))
        order = [(self.group_slicing[i], self.group_slicing[j]) for i, j in order_rep]
        labels_new = deepcopy(self.labels)
        eq_sep = deepcopy(self.eq_sep)
        slicing_indices = []
        for i in range(len(self.sliced_edges)):
            m, n = self.sliced_edges[i]
            idxm_n, idxn_m = labels_new[m].index(n), labels_new[n].index(m)
            slicing_indices.append((idxm_n, idxn_m))
            labels_new[m].pop(idxm_n)
            labels_new[n].pop(idxn_m)
            eq_sep[m] = eq_sep[m][:idxm_n] + eq_sep[m][idxm_n+1:]
            eq_sep[n] = eq_sep[n][:idxn_m] + eq_sep[n][idxn_m+1:]
        order = order_merge(order, eq_sep)
        scheme, eq_slicing = contraction_scheme(eq_sep, order)

        slice_tensor_sum = 0
        tensors_torch = []
        for i in range(len(self.labels)):
            tensors_torch.append(torch.from_numpy(self.tensors[i]).to(self.dtype).to(self.device))
        for s in range(segment * 2**task_num, (segment + 1) * 2**task_num):
            # torch.cuda.synchronize(self.device)
            # t0 = time.time()
            # eq, shapes, _, _ = self.model._labels_to_einsum()
            # eq_sep_new = eq.split('->')[0].split(',')
            bitstring = list(map(int, binary_repr(s, len(self.sliced_edges))))
            sliced_tensors = tensors_torch.copy()
            for i in range(len(self.sliced_edges)):
                m, n = self.sliced_edges[i]
                idxm_n, idxn_m = slicing_indices[i]
                sliced_tensors[m] = sliced_tensors[m].select(idxm_n, bitstring[i])
                sliced_tensors[n] = sliced_tensors[n].select(idxn_m, bitstring[i])

            # order_new = order_merge(order, eq_sep)
            torch.cuda.synchronize(self.device)
            t1 = time.time()
            # tc, tcs , sc, scs, tt, max_dim, min_dim, _, eq_slicing = normal_contraction(sliced_tensors, deepcopy(eq_sep), order)
            tc, tcs, sc, scs, tt, _ = tensor_contraction(sliced_tensors, scheme)
            torch.cuda.synchronize(self.device)
            t_calculation += time.time() - t1
            # t_all = time.time() - t0
            # print('tc {} sc {} calculation time {} all time {}'.format(tc, sc, t_cal, t_all))
            if type(slice_tensor_sum) is int:
                slice_tensor_sum = sliced_tensors[order[-1][0]].cpu().to(torch.complex128)
            else:
                slice_tensor_sum += sliced_tensors[order[-1][0]].cpu().to(torch.complex128)
            del sliced_tensors
        
        torch.cuda.synchronize(self.device)
        t_end = time.time()
        time_spent = t_end - t_start
        torch.save((slice_tensor_sum, time_spent, t_calculation, eq_slicing), data_filename)
        print('task {} all time {} calculation time {}'.format(segment, time_spent, t_calculation))
        
        return slice_tensor_sum, eq_slicing


    def slicing_subtasks_cut(self, segment, task_num=11):
        '''
        employ subtasks for contraction of slicing group, 
        each one will calculate 2**11 subtasks and add all resulting tensors together and store it.
        :param task_num: indicate which subtask this function will run
        '''
        data_filename = join(dirname(__file__), 'slicing_components/n{}_m{}_s{}_{}_s2{}_sm{}_{}gpulimit_{}_data{}_{}.pt'.format(
            self.n, self.m, self.seed, self.seq, self.seed2, self.seed_mcmc, 'simplify_' if self.simplify else '', 
            self.gpu_limit, '_complex128' if self.complex128 else '_complex64', segment
        ))
        torch.cuda.synchronize(self.device)
        t_start = time.time()
        t_calculation = 0

        sliced_edges_on_cut = []
        eq_on_cut = ''
        for i in range(len(self.sliced_edges)):
            edge = self.sliced_edges[i]
            if (edge[0] in self.group_mcmc and edge[1] in self.group_slicing) or (edge[1] in self.group_mcmc and edge[0] in self.group_slicing):
                sliced_edges_on_cut.append(edge)
                eq_on_cut += self.eq_sep[edge[0]][self.labels[edge[0]].index(edge[1])]

        group_dict, l, order_rep = find_community_order_rearrange(self.order_slicing, range(len(self.group_slicing)))
        order = [(self.group_slicing[i], self.group_slicing[j]) for i, j in order_rep]
        labels_new = deepcopy(self.labels)
        eq_sep = deepcopy(self.eq_sep)
        slicing_indices = []
        for i in range(len(self.sliced_edges)):
            m, n = self.sliced_edges[i]
            idxm_n, idxn_m = labels_new[m].index(n), labels_new[n].index(m)
            slicing_indices.append((idxm_n, idxn_m))
            labels_new[m].pop(idxm_n)
            labels_new[n].pop(idxn_m)
            eq_sep[m] = eq_sep[m][:idxm_n] + eq_sep[m][idxm_n+1:]
            eq_sep[n] = eq_sep[n][:idxn_m] + eq_sep[n][idxn_m+1:]
        order = order_merge(order, eq_sep)
        scheme, eq_slicing = contraction_scheme(eq_sep, order)

        slice_tensor_sum = torch.zeros(
            [2] * (len(sliced_edges_on_cut) + len(eq_slicing)), 
            dtype=torch.complex64,
            device=self.device
        ).reshape([2**len(sliced_edges_on_cut)] + [2] * len(eq_slicing))
        tensors_torch = []
        for i in range(len(self.labels)):
            tensors_torch.append(torch.from_numpy(self.tensors[i]).to(self.dtype).to(self.device))
        for s in range(segment * 2**task_num, (segment + 1) * 2**task_num):
            # torch.cuda.synchronize(self.device)
            # t0 = time.time()
            # eq, shapes, _, _ = self.model._labels_to_einsum()
            # eq_sep_new = eq.split('->')[0].split(',')
            bitstring = list(map(int, binary_repr(s, len(self.sliced_edges))))
            sliced_tensors = tensors_torch.copy()
            for i in range(len(self.sliced_edges)):
                m, n = self.sliced_edges[i]
                idxm_n, idxn_m = slicing_indices[i]
                sliced_tensors[m] = sliced_tensors[m].select(idxm_n, bitstring[i])
                sliced_tensors[n] = sliced_tensors[n].select(idxn_m, bitstring[i])

            # order_new = order_merge(order, eq_sep)
            torch.cuda.synchronize(self.device)
            t1 = time.time()
            # tc, tcs , sc, scs, tt, max_dim, min_dim, _, eq_slicing = normal_contraction(sliced_tensors, deepcopy(eq_sep), order)
            tensor_contraction(sliced_tensors, scheme)
            torch.cuda.synchronize(self.device)
            t_calculation += time.time() - t1
            # t_all = time.time() - t0
            # print('tc {} sc {} calculation time {} all time {}'.format(tc, sc, t_cal, t_all))
            slice_tensor_sum[s // 2 ** (len(self.sliced_edges) - len(sliced_edges_on_cut))] += sliced_tensors[order[-1][0]]#.to(torch.complex128)

            del sliced_tensors
        slice_tensor_sum = slice_tensor_sum.reshape([2] * (len(sliced_edges_on_cut) + len(eq_slicing)))
        torch.cuda.synchronize(self.device)
        t_end = time.time()
        time_spent = t_end - t_start

        eq_slicing = eq_on_cut + eq_slicing
        # torch.save((slice_tensor_sum, time_spent, t_calculation, eq_slicing), data_filename)
        print('{} all time {} calculation time {}'.format(segment, time_spent, t_calculation))
        
        return slice_tensor_sum, eq_slicing
    
    
    def batch_sampling_cut(self, tensor_slicing, eq_slicing, segment):
        tensors, labels, _ = get_tensors(self.n, self.m, self.seed, seq=self.seq, bitstring=self.bitstring, simplify=False)
        l_tensors = len(tensors)
        group_sampling = []
        for node in self.group_mcmc:
            group_sampling += self.qubits_representation[self.remain_nodes[node]]
        
        tensors_torch = []
        labels_sampling = []
        for i in group_sampling:
            tensors_torch.append(torch.from_numpy(tensors[i]).to(tensor_slicing.dtype).to(self.device))
        
        final_qubits = list(range(len(labels) - self.n, len(labels)))
        closed_group = []
        qubits_sampling = []
        slicing_opposite_indices = []
        for i in range(len(group_sampling)):
            neighbor = labels[group_sampling[i]]
            tmp = []
            for node in neighbor:
                if node in group_sampling:
                    tmp.append(group_sampling.index(node))
                else:
                    tmp.append(len(group_sampling)) # point to tensor_slicing, which will be put into the end of tensors_torch
                    slicing_opposite_indices.append((i, node))
            assert len(tmp) == len(neighbor)
            labels_sampling.append(tmp)
            if group_sampling[i] in final_qubits:
                qubits_sampling.append(group_sampling[i])
            else:
                closed_group.append(i)
        qubits_sampling.sort()
        label_slicing = []
        for symbol in eq_slicing:
            edge = self.model.edges[char2idx(symbol)]
            if edge[0] in self.group_slicing:
                slicing_node, target_node = edge[0], edge[1]
            elif edge[1] in self.group_slicing:
                slicing_node, target_node = edge[1], edge[0]
            else:
                raise ValueError('Error occurs in equation slicing')
            for idx, node in slicing_opposite_indices:
                if node in self.qubits_representation[self.remain_nodes[slicing_node]] and group_sampling[idx] in self.qubits_representation[self.remain_nodes[target_node]]:
                    label_slicing.append(idx)
        assert len(label_slicing) == len(eq_slicing)
        labels_sampling.append(label_slicing)
        tensors_torch.append(tensor_slicing.to(self.device))
        assert len(labels_sampling) == len(tensors_torch)
        closed_group.append(len(labels_sampling) - 1)

        model_sampling = Contraction(tensors_torch, labels_sampling)
        tc, sc, order_sampling = model_sampling.contraction_one_community(closed_group, strategy='max_reduce_tri', seed=0)

        eq, _, _, _ = model_sampling._labels_to_einsum()
        eq_sep = eq.split('->')[0].split(',')
        scheme, eq_sampling = contraction_scheme(eq_sep, order_sampling)
        assert len(eq_sampling) == len(qubits_sampling)

        tc, tcs, sc, scs, time_spend, tensor_sampling = tensor_contraction(tensors_torch, scheme)

        idx_open_qubits = np.empty(len(eq_sampling), dtype=np.int)
        for i in range(len(eq_sampling)):
            edge = model_sampling.edges[char2idx(eq_sampling[i])]
            if group_sampling[edge[0]] in qubits_sampling:
                idx_open_qubits[qubits_sampling.index(group_sampling[edge[0]])] = i
            elif group_sampling[edge[1]] in qubits_sampling:
                idx_open_qubits[qubits_sampling.index(group_sampling[edge[1]])] = i
            else:
                raise ValueError('Error occurs in small head contraction!')
            
        tensor_sampling = tensor_sampling.permute(tuple(idx_open_qubits)).reshape(-1)
        amplitude = tensor_sampling.cpu().numpy().reshape(-1)
        amplitude_filename = join(dirname(__file__), 'slicing_components/n{}_m{}_s{}_{}_s2{}_sm{}_{}gpulimit_{}_data{}_{}.txt'.format(
            self.n, self.m, self.seed, self.seq, self.seed2, self.seed_mcmc, 'simplify_' if self.simplify else '', 
            self.gpu_limit, '_complex128' if self.complex128 else '_complex64', segment
        ))
        # np.savetxt(amplitude_filename, amplitude)
        return amplitude
    
    def cut_in_final(self, segment, task_num=11):
        tensor_slicing, eq_slicing = self.slicing_subtasks_cut(segment, task_num)
        idx_open_qubits = np.empty(len(eq_slicing), dtype=np.int)
        for i in range(len(eq_slicing)):
            edge = self.model.edges[char2idx(eq_slicing[i])]
            idx = self.group_mcmc.index(edge[0]) if edge[0] in self.group_mcmc else self.group_mcmc.index(edge[1])
            idx_open_qubits[idx] = i
        tensor_slicing = tensor_slicing.permute(tuple(idx_open_qubits)).reshape(-1)
        amplitude = tensor_slicing.reshape(-1)

        # np.savetxt(amplitude_filename, amplitude)
        return amplitude


if __name__ == "__main__":
    model = SycamoreBipartitionBatch(**vars(args))
    if not exists(model.data_filename):
        for i in range(args.task_start, args.task_end):
            tensor_slicing, eq_slicing = model.slicing_subtasks_cut(i, args.task_num)
            model.batch_sampling_cut(tensor_slicing, eq_slicing, i)
    else:
        model.batch_sampling()