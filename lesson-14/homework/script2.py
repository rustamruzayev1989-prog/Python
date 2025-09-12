import requests

API_KEY = "ВАШ_API_KEY"  # вставьте ваш ключ
CITY = "Tashkent"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    print(f"Погода в {CITY}: {description}")
    print(f"Температура: {temp}°C")
    print(f"Влажность: {humidity}%")
else:
    print("Ошибка получения данных:", response.status_code)
