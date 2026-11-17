import numpy as np
import timeit

#3.1

filename = 'data.bin'
shape = (1000, 1000)
dtype = np.float64
arr = np.memmap(filename, dtype=dtype, mode='w+', shape=shape)
arr[:] = np.random.uniform(0, 1, size=shape)
arr.flush()

#3.2

arr = np.memmap(filename, dtype=dtype, mode='r+', shape=shape)
row = arr[667, :10]
col = arr[:10, 667]
print(row)
print(col)

#3.3
time_rows = timeit.timeit(lambda: arr.sum(axis=1), number=30)

time_cols = timeit.timeit(lambda: arr.sum(axis=0), number=30)

print(f"По строкам: {time_rows:.4f} сек")
print(f"По столбцам: {time_cols:.4f} сек")