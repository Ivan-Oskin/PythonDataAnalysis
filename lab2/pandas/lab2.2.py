from data import df

print(df, "\n")

#1

print(df[df['department'] == 'IT'][['name', 'salary']], "\n")

#2

iloc = df.iloc[:3, :2]
print(iloc, "\n")

#3

print(df[df['salary'] > 70000], "\n")

#4

df['total_comp'] = df['salary'].fillna(0) + df['bonus'].fillna(0)
print(df[['name', 'salary', 'bonus', 'total_comp']], "\n")

#5

df = df.drop('hire_date', axis=1)
print(df)

