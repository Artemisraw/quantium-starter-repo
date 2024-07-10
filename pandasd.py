import pandas as pd
import csv
import glob

data_folder = "data"
dest_file = "result.csv"
collums = ['sales', 'date', 'region']
csv_files = glob.glob(f"{data_folder}/*.csv")

for csv_file in csv_files:
    df = pd.read_csv(csv_file , usecols = ['product', 'quantity', 'price', 'date', 'region'])

    df = df.iloc[1:]
    
    df['price'] = df['price'].str.replace('^\$', '', regex=True)
    df['price'] = df['price'].astype(float)
    df['sales'] = df['price'] * df['quantity']
    
    result = df[df['product'] == "pink morsel"]
    #final_df = result.groupby('region')
    final_df = result[collums]

    final_df.to_csv(dest_file, mode='a',index=False)
    print(final_df)

#print(csv_files)
