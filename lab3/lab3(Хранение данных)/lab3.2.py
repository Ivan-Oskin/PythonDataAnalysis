import pandas as pd
from data import df
import os

#1
os.makedirs('csv', exist_ok=True)
df.to_csv('csv/df.csv')
df.to_csv('csv/df_no_index.csv', index=False)

#2

df_read = pd.read_csv('csv/df.csv')
df_no_index = pd.read_csv('csv/df_no_index.csv')
print("Типы данных: \n", df.dtypes, "\n\n", df_read.dtypes, "\n")

#3

size_with_index = os.path.getsize('csv/df.csv')
size_no_index = os.path.getsize('csv/df_no_index.csv')

print("Размер файла с индексом: ", size_with_index)
print(f"Размер файла без индекса: ", size_no_index, "\n")

#4

df_fast = pd.read_csv(
    'csv/df.csv',
    dtype={
        'name': 'str',
        'salary': 'float64',
        'department': 'str',
    },
    parse_dates=['hiredate'],
    usecols=['name', 'salary', 'hiredate' ,'department'],
)

print(df_fast)



