my_dict = {"olma": 2, "olcha": 1,"anor": 4, "behi": 3}
sorted_dict = sorted((my_dict.items()),key=lambda x: x[1])
print(sorted_dict)
my_dict = {"olma": 2, "olcha": 1,"anor": 4, "behi": 3}
sorted_dict = sorted((my_dict.items()),key=lambda x: x[1], reverse=True)
print(sorted_dict)



dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}
print(result)
