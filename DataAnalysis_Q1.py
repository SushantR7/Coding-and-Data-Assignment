import pandas as pd
data=pd.read_csv('SalesData.csv',skiprows=1,
                 names=['UID','Date','AveragePrice','Total Volume','SKU #4046','SKU #4225','SKU #4770','Total Bags','Small Bags','Large Bags','XLarge Bags','category','year','region'
])  

data['month'] = pd.DatetimeIndex(df['Date']).month

x=data.groupby(['Region','month').sum()  #Displays region and month with total volume summed up according to the aforementioned parameters

s = df[df['Total Volume']>1500000000]  #Data with total volume greater than $1.5 billion
