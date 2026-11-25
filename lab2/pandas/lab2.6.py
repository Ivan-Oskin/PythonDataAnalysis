from data import df

df['salary'] = df['salary'].fillna(df.groupby('department')['salary'].transform('mean'))
df['bonus'] = df['bonus'].fillna(0)
df['total_comp'] = df['salary'].fillna(0) + df['bonus'].fillna(0)

print(df, "\n")

#1

print(df.sort_values(by='total_comp', ascending=False).head(3), "\n")

#2

print(df.groupby('department')[['salary', 'bonus']].mean(), "\n")

#3

df['high_salary'] = df['salary'] > 75000
df_high_salary = df.groupby('department')['high_salary'].mean() * 100
print(df_high_salary, "\n")
