from datetime import datetime
name = input("Iltimos, ismingni kirit: ")
year_of_birth = int(input("Iltimos, tugilgan yilingni kirit: "))
current_year = datetime.now().year
age = current_year - year_of_birth
print(f"Salom, {name}! Sen {age} yoshdasan.")
txt = 'LMaasleitbtui'
result = txt[1] + txt[2] + txt[5] + txt[7] + txt[9] + txt[11]
print(result)
txt = 'MsaatmiazD'
result = txt[0] + txt[2] + txt[4] + txt[6] + txt[8] 
print(result)
txt = "I'am John. I am from London"
result = txt[21:30]
print(result)
