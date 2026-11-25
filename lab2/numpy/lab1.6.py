import numpy as np

#6.1
arr = np.arange(20)
print("массив: ", arr)
print("каждый 3 элемент: ", arr[1::3])
print("[5:15] наоборот: ", arr[5:15][::-1])
print("последние 5 наоборот: ", arr[-5:][::-1])

#6.2

arr = np.random.randint(0, 10, size=(6, 6))
print("массив 6:6\n", arr)
print("массив 2:5, 1:4\n", arr[2:5, 1:4])
print("диогональ\n", np.diagonal(arr))
rows, cols = np.indices(arr.shape)
mask = (rows + cols) % 2 == 0
print("шахматный узор\n", arr[mask])

#6.3

a = np.array([10, 20, 30, 40, 50, 60])
print("массив а: ", a)
m = np.arange(12).reshape(3, 4)
print("массив m\n", m)
mask = [0,2,4]
print("а[0,2,4]: ", a[mask])
rows = [0,1,2]
cols = [1,3,0]
print("m попарные индексы\n", m[rows, cols])
print("блок 2х2\n", m[np.ix_([0,2], [1,3])])

#6.4

x = np.random.randn(1000)
print("сумма > 1: ", np.sum(x > 1))
print("замена на 0\nотрицательных было: ", np.sum(x < 0))
x2 = x.copy()
x2[x2 < 0] = 0
print("стало: ", np.sum(x2 < 0))
mask = np.where(np.sign(x[:-2]) != np.sign(x[2:]))[0] + 1
start_sum_null = np.sum(x[mask] == 0)
x[mask] = 0
print("было измененно элементов с соседями: ", np.sum(x == 0)-start_sum_null)




