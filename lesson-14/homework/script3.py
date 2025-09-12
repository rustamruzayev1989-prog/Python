[
  {"title": "1984", "author": "George Orwell"},
  {"title": "Dune", "author": "Frank Herbert"}
]
import json
import os

FILENAME = "books.json"

def load_books():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book():
    title = input("Введите название книги: ")
    author = input("Введите автора: ")
    books.append({"title": title, "author": author})
    save_books(books)

def update_book():
    title = input("Введите название книги для обновления: ")
    for b in books:
        if b["title"].lower() == title.lower():
            b["author"] = input("Новый автор: ")
            save_books(books)
            return
    print("Книга не найдена.")

def delete_book():
    title = input("Введите название книги для удаления: ")
    for b in books:
        if b["title"].lower() == title.lower():
            books.remove(b)
            save_books(books)
            return
    print("Книга не найдена.")

books = load_books()

while True:
    print("\n1 – Добавить  2 – Обновить  3 – Удалить  4 – Показать  0 – Выход")
    choice = input("Ваш выбор: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        for b in books:
            print(f"{b['title']} — {b['author']}")
    elif choice == "0":
        break
