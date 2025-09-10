filename = "example.txt"

try:
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print("Содержимое файла:")
    print(content)

except UnicodeDecodeError as e:
    print("Ошибка кодировки при чтении файла:", e)
