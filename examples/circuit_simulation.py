from os.path import join, dirname, exists, abspath
from os import makedirs
import opt_einsum as oe
import sys

sys.path.append(abspath(dirname(__file__)).strip('examples'))
from sys import exit
import torch
from bighead import (
    get_tensors,
    Contraction,
    write_community,
    write_order,
    SycamoreBipartitionBatch,
    dynamic_slicing,
    read_order,
    read_samples
)
from bighead.args import args

'''
Commandline example:
python examples/circuit_simulation.py -n 53 -m 12 -simplify -sc 36 -tc 41 -cuda 0 # for n53m12ABCD circuit
'''


PACKAGEDIR = abspath(join(dirname(__file__), '../bighead/'))

def sycamore_circuit_simulation():
    bipartition_filename = join(PACKAGEDIR, 'slicing_order/bipartition_n{}_m{}_s{}_{}_s2{}_{}.txt'.format(
        args.n, args.m, args.seed, args.seq, args.seed2, 'simplify_' if args.simplify else '' 
    ))
    sliced_edges_filename = join(PACKAGEDIR, 'slicing_order/n{}_m{}_s{}_{}_s2{}_{}gpulimit_{}_edges.txt'.format(
        args.n, args.m, args.seed, args.seq, args.seed2, 'simplify_' if args.simplify else '', args.gpu_limit
    ))
    bipartition_order_filename = join(PACKAGEDIR, 'slicing_order/n{}_m{}_s{}_{}_s2{}_{}gpulimit_{}_ordernew.txt'.format(
        args.n, args.m, args.seed, args.seq, args.seed2, 'simplify_' if args.simplify else '', args.gpu_limit
    ))
    if not (exists(bipartition_filename) and exists(sliced_edges_filename)):
        tensors, labels, final_qubits_representation = get_tensors(args.n, args.m, seq=args.seq, simplify=args.simplify)
        tn = Contraction(tensors, labels)
        results = tn.bipartition(args.sc, args.tc, seed=args.seed2)
        if results is not None:
            tc, sc, tcs, scs, _ = tn.contraction(order=results[0].copy())
            print("Order found, tc: {:.5f}, sc: {:.1f}".format(tc, sc))
            print("tc of each steps: ", tcs)
            print("sc of each steps: ", scs)
        else:
            print("Desired order not found.")
            exit(0)

        group = results[2]
        head_idx = 0 if len(group[0]) > len(group[1]) else 1
        group_head = group[head_idx]
        final_qubits_num = [[], []]
        for i in range(2):
            for node in group[i]:
                if node in final_qubits_representation.keys():
                    final_qubits_num[i] += final_qubits_representation[node]
        print('initial partition:', group)
        print('qubits of each partition', final_qubits_num)
        print('qubits num', (len(final_qubits_num[0]), len(final_qubits_num[1])))
        print('cut size of initial partition', results[3])

        # bipartition_order_filename = join(PACKAGEDIR, 'slicing_order/bipartition_n{}_m{}_s{}_{}_s2{}_{}.txt'.format(
        #     args.n, args.m, args.seed, args.seq, args.seed2, 'simplify_' if args.simplify else '' 
        # ))

        if min(len(final_qubits_num[0]), len(final_qubits_num[1])) > 10:
            write_community(group, bipartition_filename)
            order_sliced, slicing_edges = dynamic_slicing(tn, group_head, results[0].copy(), seed_order=args.seed2, random_init=False)
            order_sliced_new = [(group_head.index(i), group_head.index(j)) for i, j in order_sliced]
            write_order(order_sliced_new, bipartition_order_filename)
            write_order(slicing_edges, sliced_edges_filename)
            num_sliced_edges = len(slicing_edges)
            # for trial in range(20):
            #     result_slicing = dynamic_slicing(tc+0.5, sc, args.n, args.m, args.seed, args.seq, args.simplify, args.gpu_limit, args.seed2)
            #     if result_slicing is not None:
            #         num_sliced_edges = result_slicing
            #         break
        else:
            print('num of open qubits is not enough, please try another partition')
            exit(1)
    else:
        num_sliced_edges = len(read_order(sliced_edges_filename))
    
    if not exists(PACKAGEDIR + '/slicing_components/'):
        makedirs(PACKAGEDIR + '/slicing_components/')
    if not exists(PACKAGEDIR + '/samples/'):
        makedirs(PACKAGEDIR + '/samples/')
    
    model = SycamoreBipartitionBatch(**vars(args))
    sliced_edges_on_cut = []
    for i in range(len(model.sliced_edges)):
        edge = model.sliced_edges[i]
        if (edge[0] in model.group_mcmc and edge[1] in model.group_slicing) or (edge[1] in model.group_mcmc and edge[0] in model.group_slicing):
            sliced_edges_on_cut.append(edge)
    '''
    for edge in sliced_edges_on_cut:
        model.sliced_edges.remove(edge)
        model.sliced_edges.insert(0, edge)
    '''
    if not exists(model.data_filename):
        subtask_filename = join(PACKAGEDIR, 'slicing_components/n{}_m{}_s{}_{}_s2{}_sm{}_{}gpulimit_{}_data{}.pt'.format(
            args.n, args.m, args.seed, args.seq, args.seed2, args.seed_mcmc, 'simplify_' if args.simplify else '', 
            args.gpu_limit, '_complex128' if args.complex128 else '_complex64'
        ))
        subtask_completed = 0
        if num_sliced_edges - len(sliced_edges_on_cut) <= args.task_num:
            args.task_num = num_sliced_edges - len(sliced_edges_on_cut)
        subtask_all = num_sliced_edges - args.task_num
        for i in range(2**subtask_all):
            if exists(subtask_filename.strip('.pt') + '_{}.pt'.format(i)):
                subtask_completed += 1
        
        if subtask_completed <= 2**subtask_all:
            for i in range(subtask_completed, 2**subtask_all):
                model.slicing_subtasks(i, task_num=args.task_num)
    
        num = 0
        cut_vector_filename = join(PACKAGEDIR, 'samples/n{}_m{}_s{}_{}_s2{}_sm{}_{}gpulimit_{}_data_{}.pt'.format(
                args.n, args.m, args.seed, args.seq, args.seed2, args.seed_mcmc, 
                'simplify_' if args.simplify else '', args.gpu_limit, 'complex128' if args.complex128 else 'complex64')
                )
        for i in range(2**subtask_all):
            if not exists(subtask_filename.strip('.pt') + '_{}.pt'.format(i)):
                print('{} not exist'.format(i))
            else:
                num += 1
        if num == 2**subtask_all:
            for i in range(2**subtask_all):
                tensor_slicing, t_all, t_gpu, eq_slicing = torch.load(subtask_filename.strip('.pt') + '_{}.pt'.format(i))
                if i == 0:
                    tensor_slicing_fixed = torch.zeros([2] * (len(sliced_edges_on_cut) + len(eq_slicing)), dtype=torch.complex128).reshape(2**len(sliced_edges_on_cut), -1)
                j = i // 2 ** (subtask_all - len(sliced_edges_on_cut))
                tensor_slicing_fixed[j] += tensor_slicing.reshape(-1)
            tensor_slicing_fixed = tensor_slicing_fixed.reshape([2] * (len(sliced_edges_on_cut) + len(eq_slicing)))
            eq_slicing_fixed = ''
            for i in range(len(sliced_edges_on_cut)):
                eq_slicing_fixed += oe.get_symbol(model.model.edges.index(model.sliced_edges[i]))
            eq_slicing_fixed += eq_slicing
        torch.save((tensor_slicing_fixed, eq_slicing_fixed), cut_vector_filename)
    if not exists(model.samples_filename):
        samples_batch, _ = model.batch_sampling()
    else:
        samples_batch = read_samples(model.samples_filename)
    
    return samples_batch
    

if __name__ == '__main__':
    sycamore_circuit_simulation()