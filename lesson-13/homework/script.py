from datetime import date
from dateutil.relativedelta import relativedelta
name = input("Как тебя зовут? ")
birth_of_year = int(input("Укажи год рождения: "))
month_of_birth = int(input("Укажи месяц рождения: "))
day_of_birth = int(input("Укажи день рождения: "))
birth_date = date(birth_of_year, month_of_birth, day_of_birth)
today = date.today()
age = relativedelta(today, birth_date)
print(f"Привет, {name}! Тебе {age.years} лет, {age.months} месяцев и {age.days} дней.")
