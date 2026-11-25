import pandas as pd
import data

#1

arr = [1,2,3,4,5]
custom = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(arr, index=custom)
print(series)

#2

df = pd.DataFrame(data.data)
print(df)

#3

print("информация об DataFrame\n")
print("первые строки:\n", df.head(1))
print("последние строки:\n", df.tail(1))
print("тип данных: \n", df.dtypes)
print("статистика\n", df.describe())