try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))

    result = a / b
    print("Результат:", result)

except ArithmeticError as e:
    print("Арифметическая ошибка:", e)
