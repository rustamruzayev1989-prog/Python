try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    
    if not (a.isdigit() and b.isdigit()):
        raise TypeError("Inputs must be numbers")

    a = int(a)
    b = int(b)

    print("Sum:", a + b)

except TypeError as e:
    print("TypeError:", e)
