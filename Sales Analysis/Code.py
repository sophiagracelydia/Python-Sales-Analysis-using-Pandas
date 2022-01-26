import matplotlib.pyplot as plt
import pandas as pd
import os

'Task:1 Merging all the 12 months of sales data into single file'
files = [file for file in os.listdir('./Data Analysis')]
all_months_data = pd.DataFrame()
for file in files:
    df = pd.read_csv("./Data Analysis/"+file)
    all_months_data = pd.concat([all_months_data, df])
all_months_data.to_csv("all_data.csv", index=False)

'Read in updated Data Frame'
all_data = pd.read_csv("all_data.csv")

'Clean up the data-------'
'To drop the rows of NAN'
nan_df = all_data[all_data.isna().any(axis=1)]
nan_df.head()
all_data = all_data.dropna(how='all')
all_data.head()

'Find Or and delete it'
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data.head()

'Convert the columns into correct datatype'
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

'Augment the data with additional columns'
'Task:2 Add a month column'
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')

'Task:3 Add a sales column'
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

'Task:4 Add a City & State column'
'''apply(lambda x: x.split(',')[1]) One more way to do the lambda function'''

def get_city(address):
    return address.split(',')[1]
def get_state(address):
    return address.split(',')[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x)+ ' ' + get_state(x))

'Prob 1: What was the best month for sales? How much was earned that month?'
results = all_data.groupby('Month').sum()

'''To describe the data in graph
import matplotlib.pyplot as plt
months = range(1, 13)
plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Months in number')
plt.show()'''

'Prob 2: What city had the number of highest sales ?'
results = all_data.groupby('City').sum()

'''
import matplotlib.pyplot as plt
cities = [city for city, df in all_data.groupby('City')]
plt.bar(cities, results['Sales'])
plt.xticks(cities, rotation='vertical', size=8)
plt.yticks(size=8)
plt.ylabel('Sales in USD ($)')
plt.xlabel('City Name')
plt.show()'''

'Prob 3: What time should we display ad to maximize likelihood of customers buying products'
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute

'''
import matplotlib.pyplot as plt
hours = [hour for hour, df in all_data.groupby('Hour')]
plt.plot(hours, all_data.groupby(['Hour']).count())
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('Number of Orders')
plt.grid() '''


'Prob 4: What Products are most often sold together'
df = all_data[all_data['Order ID'].duplicated(keep=False)]
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df = df[['Order ID', 'Grouped']].drop_duplicates()
'''
from itertools import combinations
from collections import Counter

count = Counter()
for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 3)))
for key, value in count.most_common(10):
    print(key, value) '''

'Prob 5: What product sold the most? What do you think it sold the most?'
product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']
products = [product for product, df in product_group]

import matplotlib.pyplot as plt
'''
plt.bar(products, quantity_ordered)
plt.xticks(products, rotation='vertical', size=8)
plt.xlabel('Products')
plt.ylabel('Quantity Ordered')
'''
prices = all_data.groupby('Product').mean()['Price Each']
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(products, quantity_ordered, color='g')
ax2.plot(products, prices, 'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price', color='b')
ax1.set_xticklabels(products, rotation='vertical', size=8)
plt.show()
