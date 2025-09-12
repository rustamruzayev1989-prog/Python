#Анализ JSON (чтение students.json)
[
  {"name": "Alice", "age": 20, "grade": "A"},
  {"name": "Bob",   "age": 22, "grade": "B"}
]
import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

print("Сведения о студентах:")
for s in students:
    print(f"Имя: {s['name']}, Возраст: {s['age']}, Оценка: {s['grade']}")
