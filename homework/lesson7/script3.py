def powers_of_two(N):
    k = 1
    while 2 ** k <= N:
        print(2 ** k, end=" ")
        k += 1  
powers_of_two(10)
