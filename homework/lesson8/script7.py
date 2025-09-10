try:
    num = int(input("Введите число: "))
    print("Вы ввели:", num)
except KeyboardInterrupt:
    print("\nВвод отменён пользователем (KeyboardInterrupt).")
