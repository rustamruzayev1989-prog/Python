#F = C × 9/5 + 32
#C = (F − 32) × 5/9
import numpy as np

celsius = np.array([0, 12, 45.21, 34, 99.91, 32])
print("Значения в °C:", celsius)

fahrenheit = celsius * 9/5 + 32
print("Значения в °F:", np.round(fahrenheit, 2))

back_to_celsius = (fahrenheit - 32) * 5/9
print("Обратно в °C:", np.round(back_to_celsius, 2))
