try:
    with open("statxujjat.txt") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("xato fayl topilmadi")
