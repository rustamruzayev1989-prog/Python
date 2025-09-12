import numpy as np

arr = np.random.randint(0, 101, size=10)
print("Случайный массив:", arr)

mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)
min_val = np.min(arr)
max_val = np.max(arr)

print("Среднее значение:", mean_val)
print("Медиана:", median_val)
print("Стандартное отклонение:", std_val)
print("Минимум:", min_val)
print("Максимум:", max_val)
