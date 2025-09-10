try:
	num1 = int(input("Birinchi raqamni kiriting: "))
	num2 = int(input("Ikkinchi raqamni kiriting: "))
	result = num1 / num2
	print("Bo'luv natijasi", result)
except ZeroDivisionError:
