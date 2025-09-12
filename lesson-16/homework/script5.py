import numpy as np

arr = np.array([1, 2, 3, 4])
print("Исходный массив:", arr)
print("Тип данных исходного массива:", arr.dtype)

float_arr = arr.astype(float)
print("Массив с плавающей точкой:", float_arr)
print("Тип данных нового массива:", float_arr.dtype)
