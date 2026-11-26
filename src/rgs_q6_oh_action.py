"""Signed coordinate-permutation representation of O_h."""
from itertools import permutations, product
import numpy as np

def signed_permutation_matrices():
    matrices=[]
    for perm in permutations(range(3)):
        for signs in product((-1,1), repeat=3):
            matrix=np.zeros((3,3),dtype=np.int64)
            for row,col in enumerate(perm):
                matrix[row,col]=signs[row]
            matrices.append(matrix)
    matrices.sort(key=lambda m:tuple(int(x) for x in m.ravel()))
    return tuple(matrices)
