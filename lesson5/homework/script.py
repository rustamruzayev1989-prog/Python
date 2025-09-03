year = int(input("year="))
if(year%4==0):
    print("leap year")
else:
    print("not leap year")
    if(year%100==0):
        print("leap year")
    else:
        print("not leap year")
        if(year%400==0):
            print("leap year")
        else:
            print("not leap year")
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
