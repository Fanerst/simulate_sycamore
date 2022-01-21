import cirq
import numpy as np
import copy
import networkx as nx
import sys
import torch
import time
from os.path import join, dirname, exists, abspath
from copy import deepcopy

sys.path.append(dirname(__file__))


def get_circuit(n=12, m=14, seed=0, elide=0, seq='ABCDCDAB'):
    seq = 'ABCDCDAB' if 'a' in seq or 'A' in seq else 'EFGH'
    import importlib
    fname = "Sycamore.circuit_n{}_m{}_s{}_e{}_p{}".format(n, m, seed, elide, seq)
    # print(fname)
    qc = importlib.import_module(fname)

    id_map={}
    n_qubits = 0
    for qubit in qc.QUBIT_ORDER:
        id_map[(qubit.row,qubit.col)] = n_qubits
        n_qubits += 1

    gates = []
    for moment in qc.CIRCUIT:
        for gate in moment:
            qubits = gate.qubits
            mat = cirq.unitary(gate)
            if (len(qubits) == 1):
                qubit_id = id_map[ qubits[0].row,qubits[0].col ]
                gates.append( [mat,[qubit_id]] )
            elif (len(qubits) == 2):
                qubit1_id = id_map[ qubits[0].row,qubits[0].col ]
                qubit2_id = id_map[ qubits[1].row,qubits[1].col ]
                gates.append( [mat,[qubit1_id,qubit2_id]])
            else:
                print("unknown gates !!!")
                print(gate.__str__)
                sys.exit(0)
    return gates, qc

def swap_seq(L, idx0, idx1):
    assert idx1 <= L - 1
    assert idx0 <= L - 1
    seq = list(range(L))
    if idx0 < idx1:
        seq[idx0 + 2:idx1 + 1] = seq[idx0 + 1:idx1]
        seq[idx0 + 1] = idx1
    else:
        seq[idx1:idx0] = seq[idx1 + 1:idx0 + 1]
        seq[idx0] = idx1

    return seq

def simplify_edges(tensors, neighbors, edges, dtype=np.complex128):
    for edge in edges:
        i, j = edge
        if i in neighbors[j] and j in neighbors[i]:
            flag = True
        else:
            flag = False
        if flag:
            L_i = len(neighbors[i]) - 1
            idxi_j = neighbors[i].index(j)
            idxj_i = neighbors[j].index(i)
            neighbors[i].pop(idxi_j)
            neighbors[j].pop(idxj_i)
        else:
            L_i = len(neighbors[i])
        if flag:
            tensors[i] = np.tensordot(tensors[i], tensors[j], ([idxi_j], [idxj_i]))
        else:
            tensors[i] = np.outer(tensors[i].reshape(-1), tensors[j].reshape(-1)).reshape(
                        tensors[i].shape + tensors[j].shape)

        for node in neighbors[j]:
            idxj_n = neighbors[j].index(node)
            idxn_j = neighbors[node].index(j)
            if node in neighbors[i]:
                # merge node in neighbors_i
                idxi_n = neighbors[i].index(node)
                seqi = swap_seq(len(tensors[i].shape), idxi_n, idxj_n + L_i)
                L_i -= 1
                tensors[i] = tensors[i].transpose(seqi)
                tensors[i] = tensors[i].reshape(tensors[i].shape[:idxi_n] +
                                                (-1,) + tensors[i].shape[idxi_n + 2:])

                # merge i in neighbors_node
                idxn_i = neighbors[node].index(i)
                neighbors[node].pop(idxn_j)
                seqn = swap_seq(len(tensors[node].shape), idxn_i, idxn_j)
                tensors[node] = tensors[node].transpose(seqn)
                if idxn_i < idxn_j:
                    tensors[node] = tensors[node].reshape(tensors[node].shape[:idxn_i] +
                                                          (-1,) + tensors[node].shape[idxn_i + 2:])
                else:
                    try:
                        tensors[node] = tensors[node].reshape(tensors[node].shape[:idxn_i - 1] +
                                                              (-1,) + tensors[node].shape[idxn_i + 1:])
                    except:
                        print(i, j, node, tensors[node].shape, idxn_i, idxn_j, seqn, tensors[node])
                        raise Exception('can not reshape')
            else:
                neighbors[i].append(node)
                neighbors[node][idxn_j] = i
    
        tensors[j] = []
        neighbors[j] = []

    return tensors, neighbors

def gates2tensors(gates, qubit_num, initial_states, final_states, simplify=True):
    assert gates[0][0].dtype == initial_states[0].dtype == final_states[0].dtype
    for i in range(qubit_num):
        gates.insert(0, [initial_states[qubit_num-1-i], [qubit_num-1-i]])
        gates.append([final_states[i], [i]])

    tensors = []
    labels = []
    chains = [[] for i in range(qubit_num)]
    final_qubits = [i for i in range(len(gates)-qubit_num, len(gates))]
    qubits_representation = {}

    for i in range(len(gates)):
        tensors.append(gates[i][0])
        for j in gates[i][1]:
            chains[j].append(i)
        labels.append([])
        qubits_representation[i] = [i]

    for i in range(len(chains)):
        for j in range(len(chains[i])):
            if j == 0:
                labels[chains[i][j]].append(chains[i][j + 1])
            elif j == len(chains[i]) - 1:
                labels[chains[i][j]].append(chains[i][j - 1])
            else:
                labels[chains[i][j]] += [chains[i][j + 1], chains[i][j - 1]]

    for i in range(len(tensors)):
        labels[i] = np.array(labels[i])
        if len(labels[i]) > 1:
            labels[i] = labels[i].reshape([-1, 2]).transpose().reshape(-1)
        label_unique, idx, counts = np.unique(labels[i], return_index=True, return_counts=True)
        idx = np.argsort(idx)
        label = label_unique[idx].tolist()
        counts = counts[idx]
        tensors[i] = tensors[i].reshape(2 ** counts)
        labels[i] = label

    simplify_order = []
    if simplify:
        labels_copy = deepcopy(labels)
        remove_nodes = []
        for i in range(len(chains)):
            for j in range(len(chains[i])):
                current_node = chains[i][j]
                if len(labels[current_node]) <= 2:
                    neighbor = labels[current_node][0]
                    idx1 = labels[neighbor].index(current_node)
                    idx2 = labels[current_node].index(neighbor)
                    # tensors[neighbor] = np.tensordot(tensors[neighbor], tensors[current_node], (idx1, idx2))
                    simplify_order.append((neighbor, current_node))
                    if current_node in qubits_representation.keys():
                        value = qubits_representation.pop(current_node)
                        if neighbor in qubits_representation.keys():
                            qubits_representation[neighbor] += value
                        else:
                            qubits_representation[neighbor] = value
                    labels[current_node].pop(idx2)
                    labels[neighbor].pop(idx1)
                    for k in range(len(labels[current_node])):
                        node_add = labels[current_node][k]
                        labels[neighbor].append(node_add)
                        idx = labels[node_add].index(current_node)
                        labels[node_add].pop(idx)
                        labels[node_add].insert(idx, neighbor)
                    remove_nodes.append(current_node)
                if len(labels[current_node]) != len(list(set(labels[current_node]))):
                    nodes_add = []
                    idx1 = []
                    for k in range(len(labels[current_node])):
                        if labels[current_node].count(labels[current_node][k]) > 1:
                            neighbor = labels[current_node][k]
                            idx1.append(k)
                        else:
                            nodes_add.append(labels[current_node][k])
                    idx2 = []
                    for k in range(len(labels[neighbor])):
                        if labels[neighbor][k] == current_node:
                            idx2.append(k)
                    # tensors[neighbor] = np.tensordot(tensors[neighbor], tensors[current_node], (idx1, idx2))
                    simplify_order.append((neighbor, current_node))
                    if current_node in qubits_representation.keys():
                        value = qubits_representation.pop(current_node)
                        if neighbor in qubits_representation.keys():
                            qubits_representation[neighbor] += value
                        else:
                            qubits_representation[neighbor] = value
                    idx2.sort(reverse=True)
                    for idx in idx2:
                        labels[neighbor].pop(idx)
                    labels[neighbor] += nodes_add
                    for node in nodes_add:
                        idx = labels[node].index(current_node)
                        labels[node].pop(idx)
                        labels[node].insert(idx, neighbor)
                    remove_nodes.append(current_node)

        for i in range(len(tensors)):
            if i in remove_nodes:
                continue
            current_node = i
            if len(labels[current_node]) <= 2:
                neighbor = labels[current_node][0]
                idx1 = labels[neighbor].index(current_node)
                idx2 = labels[current_node].index(neighbor)
                # tensors[neighbor] = np.tensordot(tensors[neighbor], tensors[current_node], (idx1, idx2))
                simplify_order.append((neighbor, current_node))
                if current_node in qubits_representation.keys():
                    value = qubits_representation.pop(current_node)
                    if neighbor in qubits_representation.keys():
                        qubits_representation[neighbor] += value
                    else:
                        qubits_representation[neighbor] = value
                labels[current_node].pop(idx2)
                labels[neighbor].pop(idx1)
                for k in range(len(labels[current_node])):
                    node_add = labels[current_node][k]
                    labels[neighbor].append(node_add)
                    idx = labels[node_add].index(current_node)
                    labels[node_add].pop(idx)
                    labels[node_add].insert(idx, neighbor)
                remove_nodes.append(current_node)
        for i in range(len(tensors)):
            if i in remove_nodes:
                continue
            current_node = i
            if len(labels[current_node]) != len(list(set(labels[current_node]))):
                nodes_add = []
                idx1 = []
                for k in range(len(labels[current_node])):
                    if labels[current_node].count(labels[current_node][k]) > 1:
                        neighbor = labels[current_node][k]
                        idx1.append(k)
                    else:
                        nodes_add.append(labels[current_node][k])
                idx2 = []
                for k in range(len(labels[neighbor])):
                    if labels[neighbor][k] == current_node:
                        idx2.append(k)
                # tensors[neighbor] = np.tensordot(tensors[neighbor], tensors[current_node], (idx1, idx2))
                simplify_order.append((neighbor, current_node))
                if current_node in qubits_representation.keys():
                    value = qubits_representation.pop(current_node)
                    if neighbor in qubits_representation.keys():
                        qubits_representation[neighbor] += value
                    else:
                        qubits_representation[neighbor] = value
                idx2.sort(reverse=True)
                for idx in idx2:
                    labels[neighbor].pop(idx)
                labels[neighbor] += nodes_add
                for node in nodes_add:
                    idx = labels[node].index(current_node)
                    labels[node].pop(idx)
                    labels[node].insert(idx, neighbor)
                remove_nodes.append(current_node)

        tensors_tmp, labels_tmp = simplify_edges(tensors, labels_copy, simplify_order)

        remove_nodes.sort(reverse=True)
        remain_nodes = np.arange(len(tensors)).tolist()
        for i in remove_nodes:
            remain_nodes.remove(i)

        tensors_simp, labels_simp = [], []
        for i in remain_nodes:
            assert labels[i] == labels_tmp[i]
            labels_simp.append([remain_nodes.index(j) for j in labels_tmp[i]])
            tensors_simp.append(tensors_tmp[i])

        return tensors_simp, labels_simp, qubits_representation, remain_nodes, remove_nodes, simplify_order
    else:
        return tensors, labels, qubits_representation, [i for i in range(len(labels))], [], []

def gates2tensors_openqubits(gates, qubit_num, initial_states, final_states, simplify=True, open_qubits=None):

    assert gates[0][0].dtype == initial_states[0].dtype == final_states[0].dtype
    for i in range(qubit_num):
        gates.insert(0, [initial_states[qubit_num-1-i], [qubit_num-1-i]])
        gates.append([final_states[i], [i]])

    tensors = []
    labels = []
    chains = [[] for i in range(qubit_num)]
    qubits_representation = {}

    for i in range(len(gates)):
        tensors.append(gates[i][0])
        for j in gates[i][1]:
            chains[j].append(i)
        labels.append([])
        qubits_representation[i] = [i]

    for i in range(len(chains)):
        for j in range(len(chains[i])):
            if j == 0:
                labels[chains[i][j]].append(chains[i][j + 1])
            elif j == len(chains[i]) - 1:
                labels[chains[i][j]].append(chains[i][j - 1])
            else:
                labels[chains[i][j]] += [chains[i][j + 1], chains[i][j - 1]]

    for i in range(len(tensors)):
        labels[i] = np.array(labels[i])
        if len(labels[i]) > 1:
            labels[i] = labels[i].reshape([-1, 2]).transpose().reshape(-1)
        label_unique, idx, counts = np.unique(labels[i], return_index=True, return_counts=True)
        idx = np.argsort(idx)
        label = label_unique[idx].tolist()
        counts = counts[idx]
        tensors[i] = tensors[i].reshape(2 ** counts)
        labels[i] = label

    final_qubits = [i for i in range(len(gates)-qubit_num, len(gates))]
    if open_qubits is not None:
        open_qubits = sorted(open_qubits)
        open_qubits_id = [final_qubits[i] - qubit_num for i in open_qubits]
        open_qubits_id += [final_qubits[i] for i in open_qubits]
    else:
        open_qubits_id = []

    simplify_order = []
    if simplify:
        labels_copy = deepcopy(labels)
        remove_nodes = []
        simplify_flag = False
        for i in range(len(labels)):
            if len(labels[i]) <= 2 and i not in open_qubits_id:
                simplify_flag = True

        while simplify_flag:
            for i in range(len(tensors)):
                if i in remove_nodes or i in open_qubits_id:
                    continue
                current_node = i
                if len(labels[current_node]) <= 2:
                    neighbor = labels[current_node][0]
                    idx1 = labels[neighbor].index(current_node)
                    idx2 = labels[current_node].index(neighbor)
                    # tensors[neighbor] = np.tensordot(tensors[neighbor], tensors[current_node], (idx1, idx2))
                    simplify_order.append((neighbor, current_node))
                    if current_node in qubits_representation.keys():
                        value = qubits_representation.pop(current_node)
                        if neighbor in qubits_representation.keys():
                            qubits_representation[neighbor] += value
                        else:
                            qubits_representation[neighbor] = value
                    labels[current_node].pop(idx2)
                    labels[neighbor].pop(idx1)
                    for k in range(len(labels[current_node])):
                        node_add = labels[current_node][k]
                        labels[neighbor].append(node_add)
                        idx = labels[node_add].index(current_node)
                        labels[node_add].pop(idx)
                        labels[node_add].insert(idx, neighbor)
                    remove_nodes.append(current_node)
            for i in range(len(tensors)):
                if i in remove_nodes or i in open_qubits_id:
                    continue
                current_node = i
                if len(labels[current_node]) != len(list(set(labels[current_node]))):
                    nodes_add = []
                    idx1 = []
                    for k in range(len(labels[current_node])):
                        if labels[current_node].count(labels[current_node][k]) > 1:
                            neighbor = labels[current_node][k]
                            idx1.append(k)
                        else:
                            nodes_add.append(labels[current_node][k])
                    idx2 = []
                    for k in range(len(labels[neighbor])):
                        if labels[neighbor][k] == current_node:
                            idx2.append(k)
                    # tensors[neighbor] = np.tensordot(tensors[neighbor], tensors[current_node], (idx1, idx2))
                    simplify_order.append((neighbor, current_node))
                    if current_node in qubits_representation.keys():
                        value = qubits_representation.pop(current_node)
                        if neighbor in qubits_representation.keys():
                            qubits_representation[neighbor] += value
                        else:
                            qubits_representation[neighbor] = value
                    idx2.sort(reverse=True)
                    for idx in idx2:
                        labels[neighbor].pop(idx)
                    labels[neighbor] += nodes_add
                    for node in nodes_add:
                        idx = labels[node].index(current_node)
                        labels[node].pop(idx)
                        labels[node].insert(idx, neighbor)
                    remove_nodes.append(current_node)

            simplify_flag = False
            for i in range(len(labels)):
                if len(labels[i]) <= 2 and i not in open_qubits_id and i not in remove_nodes:
                    simplify_flag = True

        tensors_tmp, labels_tmp = simplify_edges(tensors, labels_copy, simplify_order)

        remove_nodes.sort(reverse=True)
        remain_nodes = np.arange(len(tensors)).tolist()
        for i in remove_nodes:
            remain_nodes.remove(i)

        tensors_simp, labels_simp = [], []
        for i in remain_nodes:
            assert labels[i] == labels_tmp[i]
            labels_simp.append([remain_nodes.index(j) for j in labels_tmp[i]])
            tensors_simp.append(tensors_tmp[i])

        return tensors_simp, labels_simp, qubits_representation, remain_nodes, remove_nodes, simplify_order
    else:
        return tensors, labels, qubits_representation, [i for i in range(len(labels))], [], []


def get_tensors(n=53, m=14, seed=0, elide=0, seq='A', bitstring=None, 
                dtype=np.complex128, simplify=True, get_details=False, open_qubits=None):
    np.random.seed(seed)
    initial_states = np.vstack([np.array([1, 0], dtype=dtype)] * n)
    final_states = np.empty([n, 2], dtype=dtype)
    if bitstring is None:
        for i in range(n):
            final_states[i] = np.array([1, 0], dtype=dtype) \
                if np.random.rand() < 0.5 else np.array([0, 1], dtype=dtype)
    else:
        for i in range(n):
            final_states[i] = np.array([1, 0], dtype=dtype) \
                if bitstring[i] == '0' else np.array([0, 1], dtype=dtype)
    gates, qc_cirq = get_circuit(n, m, 0, seq=seq)
    if open_qubits is None:
        tensors, labels, qubits_representation, remain_nodes, remove_nodes, simplify_order = \
            gates2tensors(copy.deepcopy(gates), n, initial_states, final_states, simplify)
    else:
        tensors, labels, qubits_representation, remain_nodes, remove_nodes, simplify_order = \
            gates2tensors_openqubits(copy.deepcopy(gates), n, initial_states, final_states, simplify, open_qubits)
    final_qubits = frozenset(range(len(gates)+n, len(gates) + 2*n))
    final_qubits_representation = {}
    for key in qubits_representation.keys():
        common = frozenset(qubits_representation[key]) & final_qubits
        if len(common) != 0:
            final_qubits_representation[remain_nodes.index(key)] = [i - len(gates) - n for i in common]
    if get_details:
        return tensors, labels, final_qubits_representation, qubits_representation, remain_nodes, simplify_order
    else:
        return tensors, labels, final_qubits_representation
