import numpy as np
import math


#1.1

arr = np.array([0.1, 0.2, 0.3], dtype=np.float32)
sum_one = np.sum(arr)
value = 0.6

print(f"сумма = {float(sum_one):.20f}")
print(f"точное значение = {value:.20f}")
print(f"разница = {float(sum_one) - value}")

#1.2

print(f"eps 32 = {np.finfo(np.float32).eps}")
print(f"eps 64 = {np.finfo(np.float64).eps}")

#1.3

a = np.float32(1.0)
b = np.float32(1.0 + 1e-8)
print(f"b = {b:.15f}")
print(f"a - b = {a - b}") 
