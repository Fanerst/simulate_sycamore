# Simulating the Sycamore quantum supremacy circuit

This repo contains data we have obtained in simulating the Sycamore quantum supremacy circuits with $n=53$ qubits, $m=20$ cycles using the tensor network method proposed in [arXiv:03...](http://arxiv.org/abs/03...)

We plan to release the code soon.

## Explanation of data

1. `data/circuit_n53_m20_s0_e0_pABCDCDAB.py` is the circuit file which has been download from the [Google's data repository for the Sycamore circuits](https://datadryad.org/stash/dataset/doi:10.5061/dryad.k6t1rj8).
2. `data/bipartition_n53_m20_s0_ABCD_s24_simplify_.txt` is the initial bipartition of the simplified tensor network corresponding to Sycamore circuit with 53 qubits, 20 cycles, seed 0, elide 0 and ABCDCDAB sequence. There are two lines in the file, the first line indicates the tail partition which includes 21 open qubits, while the second line includes the head partition with 32 closed qubits. The simplification of the tensor network is done by sequentially contracting tensors with 2 or less dimensions.
3. `data/n53_m20_s0_ABCD_s24_simplify_gpulimit_30_edges.txt`  contains the 23 slicing edges which splits the overall contraction task into $2^{23}$ subtasks, each of which has space complexity $2^{30}$ hence can be contracted using  fit into 32G memory.
4. `data/n53_m20_s0_ABCD_s24_simplify_gpulimit_30_ordernew.txt` includes the contraction order. For each edge in the contraction order, say $i, j$, the $i$th and $j$th tensor in the head partition will be contracted by tracing out the shared indices. Then the resulting tensor will be put back into the $i$th position.
5. [vector.pt](http://home.itp.ac.cn/~panzhang/sycamore/vector.pt) contains the cut tensor of of the head partition whose overall dimension is $2^{23}$ and the annotations of corresponding dimensions. The file is saved using `pytorch`, one can use `torch.load` to load the data.
6. The obtained $2^{21}$ samples for the Sycamore circuits with $n=53$ qubits and $m=20$ cycles and their probabilities are listed in [probs.txt](http://home.itp.ac.cn/~panzhang/sycamore/probs.txt) file. Notice that the assignment we assign to all closed qubits are fixed to $\underbrace{0,0,0,\cdots,0}_{32}$, and the open qubit ids  are 11, 12, 13, 19, 20, 21, 22, 23, 28, 29, 30, 31, 32, 37, 38, 39, 40, 41, 44, 45, 46.

