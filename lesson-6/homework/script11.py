start = 25
end = 50
print(f"{start} va {end} o'rtasidagi butun sonlar:")
for num in range(start, end + 1):
    if num > 1:  # простые начинаются с 2
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
