from datetime import datetime, timedelta
if len(current_str.strip()) == 10:
	current_str += " 00:00"
current_dt = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
hours = int(input("Сколько часов длится встреча? "))
minutes = int(input("Сколько минут длится встреча? "))
end_dt = current_dt + timedelta(hours=hours, minutes=minutes)
print("Встреча закончится:", end_dt.strftime("%Y-%m-%d %H:%M"))
