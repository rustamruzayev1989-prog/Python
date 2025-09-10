%pip install pytz
from datetime import datetime
import pytz

def main():

    date_str = input("Введите дату и время (формат: YYYY-MM-DD HH:MM): ")
    src_tz_str = input("Введите ваш часовой пояс (например, Europe/Moscow): ")
    dst_tz_str = input("Введите целевой часовой пояс (например, Asia/Tashkent): ")

    try:
        
        naive_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

        
        src_tz = pytz.timezone(src_tz_str)
        dst_tz = pytz.timezone(dst_tz_str)

       
        src_dt = src_tz.localize(naive_dt)

      
        dst_dt = src_dt.astimezone(dst_tz)

        print(f"\nИсходное время: {src_dt.strftime('%Y-%m-%d %H:%M %Z%z')}")
        print(f"В {dst_tz_str}: {dst_dt.strftime('%Y-%m-%d %H:%M %Z%z')}")

    except Exception as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()
