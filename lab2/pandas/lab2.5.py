from data import df
import pandas as pd

print(df, "\n")

#1

managers_data = {
    'department': ['IT', 'HR', "Finance"],
    'manager' : ['Maksimov', 'To', 'Pavlov']
}

df_managers = pd.DataFrame(managers_data)

#2

df_merged = pd.merge(df, df_managers, on='department', how='left')

#3

new_employer = {
    'name':['Lev'],
    'department':['IT'],
    'salary': [100000],
    'bonus': [5000],
    'hire_date': [pd.to_datetime('2020-07-31')],
    'manager':['Maksimov']
}

df_employer = pd.DataFrame(new_employer)
df_concat = pd.concat([df_merged, df_employer])

#4

df_final = df_concat.reset_index(drop=True)
print(df_final, "\n")

