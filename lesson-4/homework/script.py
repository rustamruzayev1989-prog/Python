my_dict = {"olma": 2, "olcha": 1,"anor": 4, "behi": 3}
sorted_dict = sorted((my_dict.items()),key=lambda x: x[1])
print(sorted_dict)
my_dict = {"olma": 2, "olcha": 1,"anor": 4, "behi": 3}
sorted_dict = sorted((my_dict.items()),key=lambda x: x[1], reverse=True)
print(sorted_dict)
