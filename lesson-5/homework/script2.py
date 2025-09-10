def check_number(n):
    if n % 2 == 1:  
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:  
        print("Not Weird")
check_number(3)   
check_number(4)   
check_number(18)  
check_number(22) 
def even_numbers_with_if(a, b):
    if a % 2 == 0:
        start = a
    else:
        start = a + 1
    return list(range(start, b + 1, 2))
print(even_numbers_with_if(3, 10))  
print(even_numbers_with_if(2, 7))   
def even_numbers_no_if(a, b):
    start = a + (a % 2)  
    return list(range(start, b + 1, 2))
print(even_numbers_no_if(3, 10))  
print(even_numbers_no_if(2, 7))  
