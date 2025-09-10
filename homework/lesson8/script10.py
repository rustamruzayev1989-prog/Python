numbers = [1, 2, 3, 4, 5]

try:
    
    numbers.split()
except AttributeError as e:
    print("AttributeError:", e)
