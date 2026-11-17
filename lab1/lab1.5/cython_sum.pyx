def sum_square(double[:] arr):
    cdef double total_sum = 0
    cdef int i
    cdef int n = arr.shape[0]
    cdef double y
    for i in range(n):
        y = arr[i]
        total_sum += y**2
    return total_sum
