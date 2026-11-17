import python_sum
import cython_sum
import timeit
import numpy as np

arr = np.random.random(10**7)
p_time = timeit.timeit(lambda: python_sum.sum_square(arr), number=5)
c_time = timeit.timeit(lambda: cython_sum.sum_square(arr), number=5)

print(f"Время Python: {p_time:.5f} сек")
print(f"Время Cython: {c_time:.5f} сек")