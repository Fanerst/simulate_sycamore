import sys
from os.path import exists, abspath, dirname, join
PACKAGEDIR = abspath(dirname(__file__)).strip('examples')
sys.path.append(PACKAGEDIR)
from bighead import (
    Contraction,
    dynamic_slicing,
    get_tensors,
)
from bighead.args import args
import time

"""
Commandline example:
python examples/find_order.py -n 53 -m 20 -seed2 4 -seed_mcmc 48 -simplify -sc 53 -tc 57
"""

def find_order():
    n, m, seed, seed2, simplify, seq, gpu_memory_limit = \
        args.n, args.m, args.seed, args.seed2, args.simplify, args.seq, args.gpu_limit
    tensors, labels, final_qubits_representation = get_tensors(n, m, seed=seed, seq=seq, simplify=simplify)
    
    model = Contraction(tensors, labels)
    
    sc_target, tc_single_step_target = args.sc, args.tc
    t0 = time.time()
    results = model.bipartition(sc_target, tc_single_step_target, seed=seed2)
    print('time of finding order:', time.time() - t0)
    print(results[0], len(results[0]))
    
    if results is not None:
        tc, sc, tcs, scs, _ = model.contraction(order=results[0].copy())
        print("Order found, tc: {:.5f}, sc: {:.1f}".format(tc, sc))
        print("tc of each steps: ", tcs)
        print("sc of each steps: ", scs)
    else:
        print("Desired order not found.")

    group = results[2]
    final_qubits_num = [[], []]
    for i in range(2):
        for node in group[i]:
            if node in final_qubits_representation.keys():
                final_qubits_num[i] += final_qubits_representation[node]
    print(final_qubits_representation)
    print('initial partition:', group)
    print('qubits of each partition', final_qubits_num)
    print('qubits num', (len(final_qubits_num[0]), len(final_qubits_num[1])))
    print('cut size of initial partition', results[3])

    slicing_idx = 0 if len(group[0]) > len(group[1]) else 1
    group_slicing = group[slicing_idx]
    order_rep = results[0].copy()

    t0 = time.time()
    order_new, slicing_edges = dynamic_slicing(model, group_slicing, order_rep, gpu_memory_limit=gpu_memory_limit, seed_order=args.seed_mcmc)
    print('time of slicing:', time.time() - t0)
    
    return order_new, slicing_edges


if __name__ == '__main__':
    order, slicing_edges = find_order()