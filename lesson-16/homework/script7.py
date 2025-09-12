import numpy as np

arr = np.array([10, 20, 30])
print("Исходный массив:", arr)

new_values = [40, 50, 60, 70, 80, 90]
arr_extended = np.append(arr, new_values)

print("После добавления значений в конец массива:", arr_extended)
