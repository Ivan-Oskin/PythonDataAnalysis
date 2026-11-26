import pandas as pd
from data import df
import os

df2 = df.copy()
os.makedirs('json', exist_ok=True)

#1

df2['skills'] = [
    [
        {'language': 'Python', 'level': 'high'}
    ],
    [
        {'language': 'Recruiting', 'level': 'medium'}
    ],
    [
        {'language': 'Java', 'level': 'high'}
    ]
]

#2

df2.to_json('json/records.json', orient='records', force_ascii=False, date_format="iso")
df2.to_json('json/columns.json', orient='columns', force_ascii=False, date_format="iso")
df2.to_json('json/index.json', orient='index', force_ascii=False, date_format="iso")
df2.to_json('json/split.json', orient='split', force_ascii=False, date_format="iso")

#3

df_byte = pd.DataFrame(
    {
        'records' : [os.path.getsize('json/records.json')],
        'columns' : [os.path.getsize('json/columns.json')],
        'index' : [os.path.getsize('json/index.json')],
        'split' : [os.path.getsize('json/split.json')],
    }
)

print("размеры: \n", df_byte)

#4

df_read = pd.read_json('json/records.json', orient='records')
df_normalized = pd.json_normalize(
    df_read.to_dict(orient='records'),
    meta=['id', 'name', 'department'],
    record_path='skills',
)

print("\n", df_normalized)







