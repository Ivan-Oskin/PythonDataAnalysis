import numpy as np
import os
import timeit

def sum_rows(mas, n):
    mas_sum = 0
    for i in range(n):
        for j in range(n):
            mas_sum += mas[i, j]
    return mas_sum

def sum_cols(mas, n):
    mas_sum = 0
    for j in range(n):
        for i in range(n):
            mas_sum += mas[i, j]
    return mas_sum

def python_sum(a, b, n):
    c = []
    for i in range(n):
        c.append((a[i] + b[i]) / (a[i] - b[i] + 1))
    return c

def row_sum(a, b):
    return (a + b) / (a -b + 1)

def out_sum(a, b, n):
    out_buffer = np.empty(n)
    np.add(a, b, out=out_buffer)
    out_buffer_del = np.empty(n)
    np.subtract(a, b, out=out_buffer_del)
    out_buffer_del += 1

    np.divide(out_buffer, out_buffer_del, out=out_buffer)
    return out_buffer

filename = 'big.dat'
shape = (50000, 200)
dtype = np.float32
arr = np.memmap(filename, dtype=dtype, mode='w+', shape=shape)
arr[:] = np.random.uniform(0, 1, size=shape)
arr.flush()

#7.1

print("Сравнения размера: ", 50000*200*4, " == ", os.path.getsize(filename))

#7.2

del arr
arr = np.memmap(filename, dtype=dtype, mode='r', shape=shape)
batch_size = 1000
arr_min = 1000000000.0
arr_max = -100000000.0
arr_sum = 0.0
arr_count = 0

for i in range(0, arr.shape[0], batch_size):
    batch = arr[i:i + batch_size]

    batch_min = np.min(batch)
    batch_max = np.max(batch)
    if batch_min < arr_min:
        arr_min = batch_min
    if batch_max > arr_max:
        arr_max = batch_max

    arr_count += batch.size
    arr_sum += np.sum(batch, dtype=np.float64)

arr_average = arr_sum / arr_count
print("max: ", arr_max)
print("min: ", arr_min)
print("average: ", arr_average)

#7.3

arr_c = np.random.rand(3000, 3000).astype(np.float32)
arr_f = np.asfortranarray(arr_c)
t_rows_c = timeit.timeit(lambda: sum_rows(arr_c, 3000), number=1)
t_cols_c = timeit.timeit(lambda: sum_cols(arr_c, 3000), number=1)
t_rows_f = timeit.timeit(lambda: sum_rows(arr_f, 3000), number=1)
t_cols_f = timeit.timeit(lambda: sum_cols(arr_f, 3000), number=1)

print("Время для С по строкам: ", t_rows_c)
print("Время для C по столбцам: ", t_cols_c)
print("Время для F по строкам: ", t_rows_f)
print("Время для F по столбцам: ", t_cols_f)

#7.4

n = 10000000

a_np = np.random.rand(n)
b_np = np.random.rand(n)

t_p = timeit.timeit(lambda: python_sum(a_np, b_np, n), number=1)
t_r = timeit.timeit(lambda: row_sum(a_np, b_np), number=1)
t_o = timeit.timeit(lambda: out_sum(a_np, b_np, n), number=1)

print("время python-цикла: ", t_p)
print("время в одну строку: ", t_r)
print("время с out: ", t_o)
