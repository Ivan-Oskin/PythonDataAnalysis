import numpy as np
from scipy import sparse
import timeit

#8.1

n = 10000
shape = (5000, 5000)

row = np.random.randint(0, shape[0], size=n)
col = np.random.randint(0, shape[1], size=n)
data = np.random.rand(n)

coo = sparse.coo_matrix((data, (row, col)), shape=shape)
csr = coo.tocsr()

un_ind = np.unique(np.stack((row, col), axis=1), axis=0)
print("проверка nnz: ", len(un_ind), " == ", csr.nnz)

#8.2

n = 4000
density = 0.005

csr = sparse.random(n, n, density=density, format='csr', dtype=np.float64)
dense = csr.toarray()

print("объем памяти dense: ", dense.nbytes)
print("объем памяти для csr: ", csr.data.nbytes + csr.indices.nbytes + csr.indptr.nbytes)

v = np.random.rand(n)

t_dense = timeit.timeit(lambda: dense @ v, number=1)
t_csr = timeit.timeit(lambda: csr @ v, number=1)

print("время для csr: ", t_csr)
print("время для dense: ", t_dense)

#8.3

n = 2000
densities = [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]
times_csr = []
times_dense = []
v = np.random.rand(n)
print(f"{'Плотность':<10} | {'CSR (сек)':<12} | {'Dense (сек)':<12}")
for density in densities:
    csr = sparse.random(n, n, density=density, format='csr', dtype=np.float64)
    dense = csr.toarray()
    t_csr = timeit.timeit(lambda: csr @ v, number=3)
    times_csr.append(t_csr)
    t_dense = timeit.timeit(lambda: dense @ v, number=3)
    times_dense.append(t_dense)
    print(f"{density:<10} | {t_csr:<12.6f} | {t_dense:<12.6f}")

