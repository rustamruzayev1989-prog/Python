import pandas as pd
import numpy as np

data = {
    'Имя': ['Элис', 'Боб', 'Чарли', 'Дэвид'],
    'Возраст': [25, 30, 35, 40],
    'Город': ['Нью-Йорк', 'Сан-Франциско', 'Лос-Анджелес', 'Чикаго']
}
df = pd.DataFrame(data)

df = df.rename(columns={'Имя': 'first_name', 'Возраст': 'age'})

print("Первые 3 строки:\n", df.head(3), "\n")

print("Средний возраст:", df['age'].mean(), "\n")

print("Столбцы first_name и Город:\n", df[['first_name', 'Город']], "\n")

np.random.seed(42)  # для повторяемости
df['Зарплата'] = np.random.randint(50000, 100000, size=len(df))
print("DataFrame с зарплатой:\n", df, "\n")

print("Сводная статистика:\n", df.describe(include='all'))
