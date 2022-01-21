from os.path import join, dirname, exists, abspath
from os import makedirs
from numpy import binary_repr
import sys
sys.path.append(abspath(dirname(__file__)).strip('examples'))
import time
import numpy as np
import torch
from bighead import (
    SycamoreBipartitionBatch,
    fix_bitstring,
)
from bighead.args import args

'''
Commandline example:
python examples/full_amplitude.py -n 38 -m 14 -seed2 3 -simplify -seq EFGH -cuda 0 # for n38m14EFGH circuit
python examples/full_amplitude.py -n 43 -m 14 -simplify -seq EFGH -seed2 2 -cuda 0 # for n43m14EFGH circuit, can reproduce results in the paper
python examples/full_amplitude.py -n 50 -m 14 -simplify -seq EFGH -seed2 5 -cuda 0 # for n50m14EFGH circuit, can reproduce results in the paper, the three examples above need GPU with 32GB memory
python examples/full_amplitude.py -n 50 -m 14 -simplify -seq EFGH -seed2 6 -cuda 0 -gpu_limit 29 # for n50m14EFGH circuit, and GPU memory less than 32GB
'''

PACKAGEDIR = abspath(join(dirname(__file__), '../bighead/'))

model = SycamoreBipartitionBatch(**vars(args))
open_qubits, length_open_qubits = sorted(model.final_qubits_mcmc), len(model.final_qubits_mcmc)
closed_qubits, length_closed_qubits = sorted(model.final_qubits_slicing), len(model.final_qubits_slicing)
print('open qubits: ', open_qubits, length_open_qubits)
print('closed qubits: ', closed_qubits, length_closed_qubits)

sliced_edges_on_cut = []
for i in range(len(model.sliced_edges)):
    edge = model.sliced_edges[i]
    if (edge[0] in model.group_mcmc and edge[1] in model.group_slicing) or (edge[1] in model.group_mcmc and edge[0] in model.group_slicing):
        sliced_edges_on_cut.append(edge)
print('num of sliced edges: ', len(model.sliced_edges))
print('num of sliced edges on cut: ', len(sliced_edges_on_cut), sliced_edges_on_cut)

bin_max, bin_min, amp_num = 0, 0, 0

for seed_closed_qubits in range(args.task_start * 2 ** args.task_num, args.task_end * 2 ** args.task_num):# range(2**length_closed_qubits):
    # torch.cuda.synchronize(model.device)
    # t0 = time.time()
    bitstring_closed_qubits = binary_repr(seed_closed_qubits, length_closed_qubits)
    args.seed_mcmc = int(fix_bitstring('0'*args.n, closed_qubits, bitstring_closed_qubits), 2)
    # print(args.seed_mcmc)
    model = SycamoreBipartitionBatch(**vars(args))
    # print('current bitstring: ', model.bitstring, 'current closed bitstring: ', bitstring_closed_qubits, seed_closed_qubits)
    # tensor_slicing, eq_slicing = model.slicing_subtasks_cut(0, len(model.sliced_edges))
    # amplitude = model.batch_sampling_cut(tensor_slicing, eq_slicing, 0)
    amplitude = model.cut_in_final(0, len(model.sliced_edges))
    amp_num += len(amplitude)
    print(f'subtask {seed_closed_qubits} completed, {amp_num} amplitudes collected')
    prob = torch.abs(amplitude) ** 2
    if args.n == 50:
        bin_min, bin_max = 8.005004985737413e-27, 5.2105216503755235e-14
    elif args.n == 43 and len(open_qubits) == 29:
        bin_min, bin_max = 1.107210835341617e-24, 7.0064227856991845e-12
    else:
        if bin_max == 0:
            bin_max = prob.max().item() * 3
            bin_min = prob.min().item() / 100
    if seed_closed_qubits == args.task_start * 2 ** args.task_num:
        hist = torch.histc(prob, bins=10000, max=bin_max, min=bin_min)
    else:
        hist += torch.histc(prob, bins=10000, max=bin_max, min=bin_min)
    del amplitude, prob
    # print(hist)
    # torch.cuda.synchronize(model.device)
    # t1 = time.time()
    # print(t1 - t0)

if not exists(join(dirname(__file__), 'data/')):
    makedirs(join(dirname(__file__), 'data/'))
np.savetxt(join(
    dirname(__file__), 
    f'../data/hist_n{args.n}m{args.m}s{args.seed}_{len(open_qubits)}_{args.task_start}_{args.task_end}_{args.task_num}.txt'), 
            hist.cpu())
