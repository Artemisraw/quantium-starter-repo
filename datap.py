import csv
with open('data/daily_sales_data_0.csv', newline = '', encoding='utf-8') as file:
    render = csv.reader(file)
    for row in render:
        while row[0] == 'pink morsel':
            quantity = float(row[2])
            print(quantity)
            break
