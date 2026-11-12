import numpy as np

#2.1

A = np.arange(20).reshape(4, 5)
print(A)
print("вторая строка", A[1])
print("столбец с индексом 3", A[:,3])
print("\n1-3; 2-4\n", A[1:4, 2:5])

#2.2

row = np.array([0,2,3])
col = np.array([1, 4])
print("\nfancy:\n", A[np.ix_(row, col)])

#2.3

arr = np.array([[-1, 2, -3], [4, -5, 6]])
print("логическая индексация\n", arr)
arr[arr < 0] = 0
print("измененный массив\n", arr)

#2.4
print("broadcast\n")
B = np.arange(4).reshape(4, 1)
C = np.arange(5).reshape(1, 5)
print("B = ", B)
print("C = ", C)
print("B+C\n", B+C)



