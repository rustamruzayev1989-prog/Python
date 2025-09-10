i = 1
while i <= 10:
    print(i)
    i += 1
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
n = int(input("Enter number "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum is:", total)
