import pandas as pd
from data import df
import os
import timeit

os.makedirs('final', exist_ok=True)

t_csv_write = timeit.timeit(lambda: df.to_csv('final/df.csv'), number=1)
t_json_write = timeit.timeit(lambda: df.to_json('final/df.json',
                                               orient='records',
                                               force_ascii=False,
                                               date_format="iso"), number=1)
t_parquet_write = timeit.timeit(lambda: df.to_parquet('final/df.parquet', compression='snappy'), number=1)
t_hdf_write = timeit.timeit(lambda: df.to_hdf('final/df.h5', key='df', mode='w', format='fixed'), number=1)

t_csv_read = timeit.timeit(lambda: pd.read_csv('final/df.csv'), number=1)
t_json_read = timeit.timeit(lambda: pd.read_json('final/df.json', orient='records'), number=1)
t_parquet_read = timeit.timeit(lambda: pd.read_parquet('final/df.parquet'), number=1)
t_hdf_read = timeit.timeit(lambda: pd.read_hdf(
    'final/df.h5',
    key='df'), number=1)

df_final = pd.DataFrame(
    {
        'size' : [
            os.path.getsize('final/df.csv'),
            os.path.getsize('final/df.json'),
            os.path.getsize('final/df.parquet'),
            os.path.getsize('final/df.h5')
        ],
        'time_write': [
            t_csv_write,
            t_json_write,
            t_parquet_write,
            t_hdf_write,
        ],
        'time_read': [
            t_csv_read,
            t_json_read,
            t_parquet_read,
            t_hdf_read,
        ]
    },
    index=['CSV', 'JSON', 'Parquet', 'HDF5']
)

print(df_final)
