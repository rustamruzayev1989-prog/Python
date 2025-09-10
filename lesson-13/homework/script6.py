import re

def validate_email(email: str) -> bool:
   
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def main():
    email = input("Введите адрес электронной почты: ").strip()

    if validate_email(email):
        print("Email корректный!")
    else:
        print("Неверный формат email!")

if __name__ == "__main__":
    main()
