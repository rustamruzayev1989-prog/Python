import sqlite3

# 1️⃣ Создание (или подключение к существующей) базы данных
conn = sqlite3.connect("crew.db")
cursor = conn.cursor()

# 2️⃣ Создание таблицы Roster
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Имя TEXT,
    Вид TEXT,
    Возраст INTEGER
)
""")

# 3️⃣ Заполнение таблицы начальными данными
data = [
    ("Бенджамин Сиско", "Человек", 40),
    ("Джадзия Дакс", "Трель", 300),
    ("Кира Нерис", "баджорский", 29)
]
cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", data)
conn.commit()

# 4️⃣ Обновление имени Джадзии Дакс на Эзри Дакс
cursor.execute("""
UPDATE Roster
SET Имя = 'Эзри Дакс'
WHERE Имя = 'Джадзия Дакс'
""")
conn.commit()

# 5️⃣ Отображение имени и возраста всех баджорцев
cursor.execute("""
SELECT Имя, Возраст
FROM Roster
WHERE Вид = 'баджорский'
""")
results = cursor.fetchall()

print("Баджорцы в таблице Roster:")
for row in results:
    print(f"Имя: {row[0]}, Возраст: {row[1]}")

# Закрываем соединение
conn.close()
