import numpy as np
import os
import math
import copy
import torch
import time

_einsum_symbols_base = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXTZ'

def char2idx(char):
    if char in _einsum_symbols_base:
        return _einsum_symbols_base.index(char)
    return ord(char) - 140

def read_order(filename):
    if os.path.exists(filename):
        order = []
        with open(filename, 'r') as f:
            l = f.readlines()
        f.close()
        for line in l:
            ll = line.split()
            order.append((int(ll[0]), int(ll[1])))
        return order
    else:
        raise ValueError("{} does not exist".format(filename))


def write_order(order, filename):
    with open(filename, 'w') as f:
        for edge in order:
            f.write("%d %d \n" % (edge[0], edge[1]))
    f.close()


def read_community(filename):
    if os.path.exists(filename):
        communities = []
        with open(filename, 'r') as f:
            l = f.readlines()
        f.close()
        for line in l:
            ll = line.split()
            communities.append(list(map(int, ll)))
        if len(communities) == 1:
            communities = communities[0]
        return communities
    else:
        raise ValueError("{} does not exist".format(filename))


def write_community(community, filename):
    with open(filename, 'w') as f:
        if any(isinstance(item, list) for item in community):
            for com in community:
                for node in com:
                    f.write("%d " % (node))
                f.write('\n')
        else:
            for node in community:
                f.write(f'{node:d} ')
            f.write('\n')
    f.close()

def read_samples(filename):
    if os.path.exists(filename):
        samples_data = []
        with open(filename, 'r') as f:
            l = f.readlines()
        f.close()
        for line in l:
            ll = line.split()
            if len(ll) == 3:
                samples_data.append((ll[0], float(ll[1]), complex(ll[2])))
            else:
                samples_data.append((ll[0], float(ll[1])))
        return samples_data
    else:
        raise ValueError("{} does not exist".format(filename)) 

def write_samples(samples_data, filename):
    with open(filename, 'w') as f:
        for i in range(len(samples_data)):
            f.write("{} {} {}\n".format(samples_data[i][0], samples_data[i][1], samples_data[i][2]))
    f.close()


def log10sumexp2(s):
    s = np.array(s)
    if len(s) == 0:
        return 0
    else:
        ms = max(s)
        return np.log10(sum(np.exp2(s - ms))) + ms * np.log10(2)


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


def move_end_seq(L, idx):
    assert idx <= L - 1
    seq = list(range(L))
    if idx == L - 1:
        return seq, seq
    else:
        return seq[idx + 1:] + seq[:idx + 1], seq[-(idx + 1):] + seq[:-(idx + 1)]


def prod(list):
    results = 1
    for number in list:
        results *= number

    return results


def item_product(item_list):
    result = [[]]
    for l in range(len(item_list)):
        result = [x + [y] for x in result for y in item_list[l]]
    
    return result


# def ctg2normal(ctg_order):
#     sub = np.arange(len(ctg_order)+1).tolist()
#     order = []
#     for edge in ctg_order:
#         i, j = edge
#         order.append((sub[i], sub[j]))
#         sub.pop(j)
#         m = sub.pop(i)
#         sub.append(m)
#     return order


# def normal2ctg(order):
#     order_ctg = []
#     idx = np.arange(len(order)+1).tolist()

#     for edge in order:
#         i, j = edge
#         a, b = idx.index(i), idx.index(j)
#         order_ctg.append((a, b))
#         idx.remove(i)
#         idx.remove(j)
#         idx.append(i)

#     return order_ctg
