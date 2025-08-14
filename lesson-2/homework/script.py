from datetime import datetime
name = input("Iltimos, ismingni kirit: ")
year_of_birth = int(input("Iltimos, tugilgan yilingni kirit: "))
current_year = datetime.now().year
age = current_year - year_of_birth
print(f"Salom, {name}! Sen {age} yoshdasan.")
