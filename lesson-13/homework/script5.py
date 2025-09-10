from datetime import datetime
import time

def countdown_timer():
    
    target_str = input("Введите дату и время окончания (формат: YYYY-MM-DD HH:MM:SS): ")

    try:
        target_time = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

        while True:
            now = datetime.now()
            diff = target_time - now

            if diff.total_seconds() <= 0:
                print("\n Время вышло!")
                break

           
            days = diff.days
            hours, remainder = divmod(diff.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            print(f"\rОсталось: {days}д {hours:02d}:{minutes:02d}:{seconds:02d}", end="")

            time.sleep(1)

    except ValueError:
        print(" Неверный формат даты! Используйте YYYY-MM-DD HH:MM:SS")


if __name__ == "__main__":
    countdown_timer()
