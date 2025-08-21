try:
	num1 = int(input("Birinchi raqamni kiriting: "))
	num2 = int(input("Ikkinchi raqamni kiriting: "))
	result = num1 / num2
	print("Bo'luv natijasi", result)
except ZeroDivisionError:
	print("Xato nolga bo'lish mumkin emas")
try:
    num = int(input("Iltimos raqam kiriting"))
    print("siz son kirittingiz", num)
except ValueError:
    print("siz butun son kirittingiz")
try:
    with open("statxujjat.txt") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("xato fayl topilmadi")
