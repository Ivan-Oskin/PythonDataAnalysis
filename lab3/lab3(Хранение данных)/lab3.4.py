import pandas as pd
from data import df
import os
import timeit

os.makedirs('parquet', exist_ok=True)

df.to_parquet('parquet/snappy.parquet', compression='snappy')
df.to_parquet('parquet/gzip.parquet', compression='gzip')
df.to_parquet('parquet/brotli.parquet', compression='brotli')
df.to_csv('parquet/df.csv')

#2

df_byte = pd.DataFrame(
    {
        'csv' : [os.path.getsize('parquet/df.csv')],
        'snappy' : [os.path.getsize('parquet/snappy.parquet')],
        'gzip' : [os.path.getsize('parquet/gzip.parquet')],
        'brotli' : [os.path.getsize('parquet/brotli.parquet')],
    }
)

print("размеры: \n", df_byte)

#3


t_csv = timeit.timeit(lambda: pd.read_csv('parquet/df.csv'), number=5)
t_parquet = timeit.timeit(lambda: pd.read_parquet('parquet/snappy.parquet'), number=5)

print('\nвремя для csv: ', t_csv, "\nвремя для parquet: ", t_parquet, "\n")

#4

df_subset = pd.read_parquet('parquet/snappy.parquet', columns=['name', 'salary'])
print(df_subset, "\n")

#5

df_types = pd.read_parquet('parquet/snappy.parquet')
print("типы данных: \n", df_types.dtypes)



