numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Введите индекс: "))
    print("Элемент списка:", numbers[index])
except IndexError:
    print("Ошибка: индекс выходит за пределы списка!")
