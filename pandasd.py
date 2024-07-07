import pandas as pd

df = pd.read_csv("data/daily_sales_data_0.csv", usecols = ['product', 'quantity', 'price', 'date', 'region'])

df = df.iloc[1:]

df['price'] = df['price'].str.replace('^\$', '', regex=True)
df['price'] = df['price'].astype(float)
df['sales'] = df['price'] * df['quantity']

result = df[df['product'] == "pink morsel"]
#final_df = result.groupby('region')
print(result)
