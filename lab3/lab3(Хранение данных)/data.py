import pandas as pd

data = {
    'id': [1, 2, 3],
    'name': ['Ivan', 'Lev', 'Andrew'],
    'age': [23, 34, 19],
    'salary': [50000.0, 100000.0, 20000.0],
    'department': ['HR', 'IT', 'Finance'],
    'hiredate': pd.to_datetime(['2023-01-15', '2023-05-22', '2025-11-01']),
    'is_active': [True, True, False],
}

df = pd.DataFrame(data)

