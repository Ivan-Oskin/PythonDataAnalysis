import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

df1 = pd.read_csv('orders.csv')

#7

df1['client_clean'] = df1['client'].str.strip().str.title()
df1['city_clean'] = df1['city'].str.strip().str.title()
df1['category_clean'] = df1['category'].str.strip().str.lower()
df1['product_clean'] = df1['product'].str.strip().str.upper()
df1['revenue'] = (df1['qty'] * df1['price'] * (1 - df1['discount'])).round(2)

#8

df2 = df1.copy()

df2['revenue_rank'] = df2['revenue'].rank(method='dense', ascending=False).astype(int)
df2 = df2.sort_values(by=['revenue', 'order_date'], ascending=[False, True]).reset_index(drop=True)

#9

df3 = df2.copy()

df3['order_date'] = pd.to_datetime(df3['order_date'])
df3['order_year'] = df3['order_date'].dt.year
df3['order_month'] = df3['order_date'].dt.month
df3['order_quarter'] = df3['order_date'].dt.quarter

df3['order_weekday'] = df3['order_date'].dt.day_name()

df3['is_weekend'] = df3['order_date'].dt.day_of_week >= 5

df3['delivery_date'] = df3['order_date'] + pd.to_timedelta(df3['delivery_days'], unit='D')

df3['days_to_month_end'] = (df3['order_date'] + pd.offsets.MonthEnd(0) - df3['order_date']).dt.days

#10

df4 = df3.copy()

df4['duplicate_group_flag'] = df4.duplicated(
    subset=['client_clean', 'order_date', 'product_clean'], keep=False
)

df4 = df4.sort_values(by='revenue', ascending=False)
df4 = df4.drop_duplicates(
    subset=['client_clean', 'order_date', 'product_clean'], keep='first'
)

df4 = df4.sort_values(by='order_id').reset_index(drop=True)

#11

df5 = df4.copy()

segments = [
    (df5['revenue'] >= 0) & (df5['revenue'] < 1000),
    (df5['revenue'] >= 1000) & (df5['revenue'] < 5000),
    (df5['revenue'] >= 5000) & (df5['revenue'] < 20000),
    (df5['revenue'] >= 20000)
]

segments_names = ['low', 'medium', 'high', 'vip']

df5['revenue_segment'] = np.select(segments, segments_names, default='no_status')

status_map = {
    'new': 'новый',
    'paid': 'оплачен',
    'shipped': 'отправлен',
    'cancelled': 'отменён',
    'returned': 'возврат'
}

df5['status_ru'] = df5['status'].map(status_map)

df5['promo_used'] = df5['promo_code'] != 'NO_PROMO'

#12

df6 = df5.copy()

conditions = [
    df6['status'].isin(['cancelled', 'returned']),
    (df6['revenue'] >= 20000) & (df6['delivery_days'] <= 3),
    df6['revenue'] >= 5000
]
choices = ['archive', 'A', 'B']

df6['priority'] = np.select(conditions, choices, default='C')

df6['manager_email'] = (
    df6['manager'].str.lower().str.replace(' ', '.') + '@shop.ru'
)

df6['final_comment'] = (
    df6['client_clean'] + ': ' + df6['priority'] + ', ' + df6['revenue_segment'].astype(str)
)

df6.to_csv('orders_final.csv', index=False)




