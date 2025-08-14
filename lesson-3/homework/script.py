mevalar=["olma", "nok", "olcha", "anor", "behi"]
print(mevalar[2])
list1=[1, 2, 3]
list2=[4, 5, 6]
print(list1+list2)
favorite_movies=("Terminator","The Matrix", "Inception", "Interstellar", "The Martian")
movies_tuple = tuple(favorite_movies)
print(favorite_movies)
shaharlar = ["London", "Parij", "Istaambul", "Moskva", "Praga"]
if "Parij" in shaharlar:
    print("Parij ro'yxatda bor!")
else:
    print("Parij ro'yxatda yo'q!")
numbers = [1, 2, 3, 4, 5]
doubled_numbers = numbers * 2
print(doubled_numbers)
numbers = [1, 2, 3, 4, 5]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
slice_of_numbers = numbers[3:7]
print(slice_of_numbers)
ranglar = ("oq", "qizil", "sariq", "kok", "yashil", "kok", "jigarrang")
count_kok = ranglar.count("kok")
print(f"kok : {count_kok}")
