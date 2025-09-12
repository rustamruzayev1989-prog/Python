import requests
import random

API_KEY = "ВАШ_API_KEY"
genre = input("Введите жанр фильма (например, Action, Comedy, Drama): ")
# Поиск фильмов по ключевому слову жанра
URL = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}&type=movie&page=1"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    if data.get("Search"):
        movie = random.choice(data["Search"])
        print("Рекомендую фильм:")
        print(f"Название: {movie['Title']}")
        print(f"Год: {movie['Year']}")
        print(f"Подробнее: https://www.imdb.com/title/{movie['imdbID']}/")
    else:
        print("Фильмы с таким жанром не найдены.")
else:
    print("Ошибка запроса:", response.status_code)
