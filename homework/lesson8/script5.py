filename = "test.txt"

try:
    
    with open(filename, "w") as f:
        f.write("Hello, world!")

    print("Файл успешно открыт и записан.")

except PermissionError:
    print("Ошибка: нет прав доступа к файлу", filename)
