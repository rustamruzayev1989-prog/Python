import re

def check_password_strength(password: str) -> bool:
   
    if len(password) < 8:
        print("Пароль слишком короткий (мин. 8 символов)")
        return False

    
    if not re.search(r"[A-Z]", password):
        print("Нет заглавной буквы")
        return False
    if not re.search(r"[a-z]", password):
        print("Нет строчной буквы")
        return False
    if not re.search(r"\d", password):
        print("Нет цифры")
        return False
    if not re.search(r"[@$!%*?&]", password):
        print("Нет спецсимвола (@$!%*?&)")
        return False

    return True

def main():
    password = input("Введите пароль: ")
    if check_password_strength(password):
        print("Пароль надёжный!")
    else:
        print("Попробуйте придумать другой пароль.")

if __name__ == "__main__":
    main()
