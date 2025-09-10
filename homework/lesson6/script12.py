n = 10
a, b = 0, 1
print("Fibonacci ketma-ketligi:")
for _ in range(n):
    print(a, end="  ")
    a, b = b, a + b
