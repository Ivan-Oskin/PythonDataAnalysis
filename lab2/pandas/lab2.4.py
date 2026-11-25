from data import df

print(df, "\n")

#1

print(df.groupby('department')['salary'].mean(), "\n")

#2

stats = df.groupby('department').agg(
    {
        'salary': 'mean',
        'bonus': 'max',
        'name' : 'count',
    }
)

stats.columns = ['salary_mean', 'bonus_max', 'name_count']
print(stats, "\n")

#3

salary_mean = df.pivot_table(index='department', values='salary', aggfunc='mean')
print(salary_mean, "\n")

#4

print(salary_mean.sort_values(by='salary', ascending=False), "\n")