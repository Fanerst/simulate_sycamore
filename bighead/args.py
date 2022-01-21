import argparse

parser = argparse.ArgumentParser(description='')
group = parser.add_argument_group('common arguments')
group.add_argument("-n", type=int, default=53, help="number of qubits for Sycamore, number of nodes for QAOA")
group.add_argument("-m", type=int, default=20, help="cycles of sycamore circuits")
group.add_argument("-seed", type=int, default=0, help="seed1")
group.add_argument("-seed2", type=int, default=1, help="seed2")
group.add_argument("-log", type=str, default='',help = "log file")
group.add_argument("-Dmax", type=int, default=-1, help="Maximum physical bond dimension of the tensors. With Dmax<0, contraction will be exact")
group.add_argument("-cutoff", type=float, default=1.0e-14, help="Cut off of svd")
group.add_argument("-cuda", type=int, default=-1, help="GPU #")

group = parser.add_argument_group('order arguments')
group.add_argument("-complex128", action='store_true', help="use complex128 instead of complex64")
group.add_argument("-simplify", action='store_true', help="simplify the circuit or not")
group.add_argument("-seq", type=str, default='ABCD',choices=['ABCD','EFGH'], help="circuit seqence")
group.add_argument("-sc", type=int, default=39, help="sc target")
group.add_argument("-tc", type=int, default=42, help="tc target single step")
group.add_argument("-gpu_limit", type=int, default=30, help="memory limit of GPU")
group.add_argument("-method", type=str, default='bipartition', choices=['bipartition', 'kickoff'], help="")
group.add_argument("-trials", type=int, default=1, help="number of trials")

group = parser.add_argument_group('contraction arguments')
group.add_argument("-task_start", type=int, default=0, help="start # of subtasks, each has 2**task_num subtasks")
group.add_argument("-task_end", type=int, default=16, help="end # of subtasks, each has 2**task_num subtasks")
group.add_argument("-task_num", type=int, default=11, help="# of subtasks for single run")
group.add_argument("-backend", type=str, default='torch',choices=['torch','np', 'jax'], help="backend for contraction")
group.add_argument("-order_file", type=str, default='',help = "order file")

group = parser.add_argument_group('sampling arguments')
group.add_argument("-sampling_method", type=str, default='all', choices=['mcmc', 'all'], help="")
group.add_argument("-burn_in", type=int, default=10, help="MCMC burn in steps")
group.add_argument("-num_samples", type=int, default=20, help="MCMC samples of each chain")
group.add_argument("-num_chains", type=int, default=25, help="MCMC chains")
group.add_argument("-seed_mcmc", type=int, default=0, help="seed for MCMC")

args = parser.parse_known_args()[0]#parse_args()