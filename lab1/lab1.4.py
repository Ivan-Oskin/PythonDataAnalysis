import numpy as np
from scipy import sparse
import timeit

#4.1

row  = np.array([0, 1, 2, 3, 4])
col  = np.array([0, 1, 2, 3, 4])
data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

A_csr = sparse.csr_matrix((data, (row, col)), shape=(5, 5))
print(A_csr.toarray())
print("Плотность: ", A_csr.nnz / (A_csr.shape[0] * A_csr.shape[1]))

#4.2

A_coo = A_csr.tocoo()
A_csc = A_csr.tocsc()

print("COO:\n", A_coo)
print("CSC:\n", A_csc)

#4.3

B = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

C = A_csc.dot(B)

print("C:\n", C)

#4.4

n = 1000
A_sparse = sparse.random(n, n, density=0.01, format='csr', random_state=50)
A_dense = A_sparse.toarray()
B = np.random.default_rng(50).random(n)

t_sparse = timeit.timeit(lambda: A_sparse.dot(B), number=30)
t_dense  = timeit.timeit(lambda: A_dense.dot(B),  number=30)
print(f"Разреженное: {t_sparse:.5f} сек")
print(f"Плотное: {t_dense:.5f} сек")