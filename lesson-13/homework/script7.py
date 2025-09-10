import re

def format_phone_number(number: str) -> str:
    
    digits = re.sub(r"\D", "", number)

    if len(digits) == 10:
        return f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    else:
        return "Неверный номер! Нужно 10 цифр."

def main():
    phone = input("Введите номер телефона: ")
    formatted = format_phone_number(phone)
    print("Форматированный номер:", formatted)

if __name__ == "__main__":
    main()
