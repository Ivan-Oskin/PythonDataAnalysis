from data import df

print(df, "\n")

#1
print("количество пропусков: \n", df.isnull().sum(),"\n")
#2
df['salary'] = df['salary'].fillna(df.groupby('department')['salary'].transform('mean'))
#3
df['bonus'] = df['bonus'].fillna(0)
#4
df = df.dropna(subset=['salary'])
print(df, "\n")



