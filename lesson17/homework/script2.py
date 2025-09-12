import pandas as pd

data = {
    "Месяц": ["Январь", "Февраль", "Март", "Апрель"],
    "Продажи": [5000, 6000, 7500, 8000],
    "Расходы": [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)
print("Таблица sales_and_expenses:\n", sales_and_expenses, "\n")

max_sales = sales_and_expenses["Продажи"].max()
max_expenses = sales_and_expenses["Расходы"].max()
print("Максимальные продажи:", max_sales)
print("Максимальные расходы:", max_expenses, "\n")

min_sales = sales_and_expenses["Продажи"].min()
min_expenses = sales_and_expenses["Расходы"].min()
print("Минимальные продажи:", min_sales)
print("Минимальные расходы:", min_expenses, "\n")

mean_sales = sales_and_expenses["Продажи"].mean()
mean_expenses = sales_and_expenses["Расходы"].mean()
print("Средние продажи:", mean_sales)
print("Средние расходы:", mean_expenses)
