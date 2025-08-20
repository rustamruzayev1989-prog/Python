my_dict = {"olma": 2, "olcha": 1,"anor": 4, "behi": 3}
sorted_dict = sorted((my_dict.items()),key=lambda x: x[1])
print(sorted_dict)
my_dict = {"olma": 2, "olcha": 1,"anor": 4, "behi": 3}
sorted_dict = sorted((my_dict.items()),key=lambda x: x[1], reverse=True)
print(sorted_dict)
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}
print(result)
n = int(input("Raqamni kiriting n:"))
my_dict = {}
for i in range(1, n+1):
    my_dict[i] = i*i
print(f"n uchun lug'at n={n}:")
print(my_dict)
