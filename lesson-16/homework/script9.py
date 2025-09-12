import numpy as np

np.random.seed(0)

arr = np.random.rand(10, 10)
print("Случайный массив 10x10:\n", arr)

min_val = np.min(arr)
max_val = np.max(arr)

print("\nМинимальное значение:", min_val)
print("Максимальное значение:", max_val)
