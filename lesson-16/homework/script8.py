import numpy as np


np.random.seed(0)


arr = np.random.randint(0, 101, size=10)
print("Случайный массив:", arr)


mean_val = np.mean(arr)      # среднее значение
median_val = np.median(arr)  # медиана
std_val = np.std(arr)        # стандартное отклонение

print("Среднее значение:", mean_val)
print("Медиана:", median_val)
print("Стандартное отклонение:", std_val)
