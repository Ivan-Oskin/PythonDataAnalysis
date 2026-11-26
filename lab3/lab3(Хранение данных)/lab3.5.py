import pandas as pd
from data import df
import os
import timeit

os.makedirs('HDF5', exist_ok=True)

#1

df_mean = df.groupby('department')['salary'].mean()

with pd.HDFStore("HDF5/data.h5", mode='w') as store:
    store['employees'] = df
    store['salary_mean'] = df_mean

#2

df_mean_loaded = pd.read_hdf("HDF5/data.h5", key='salary_mean')
print(df_mean_loaded, "\n")

#3

t_fixed = timeit.timeit(lambda: df.to_hdf('HDF5/data_fixed.h5', key='df', mode='w', format='fixed'), number=5)
t_table = timeit.timeit(lambda: df.to_hdf('HDF5/data_table.h5', key='df', mode='w', format='table', data_columns=['department']), number=5)

print('\nвремя для fixed: ', t_fixed, "\nвремя для table: ", t_table, "\n")

#4

df_filtered = pd.read_hdf(
    'HDF5/data_table.h5',
    key='df',
    where='department == "IT"'
)

print(df_filtered, "\n")

#5

df.to_csv('HDF5/df.csv')

df_byte = pd.DataFrame(
    {
        'csv' : [os.path.getsize('HDF5/df.csv')],
        'table' : [os.path.getsize('HDF5/data_table.h5')],
        'fixed' : [os.path.getsize('HDF5/data_fixed.h5')],
    }
)

print("размеры: \n", df_byte)
