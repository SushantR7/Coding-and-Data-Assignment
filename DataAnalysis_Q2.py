import pandas as pd
data=pd.read_csv('SalesData.csv',skiprows=1,
                 names=['UID','Date','AveragePrice','Total Volume','SKU #4046','SKU #4225','SKU #4770','Total Bags','Small Bags','Large Bags','XLarge Bags','category','year','region'
])  

data.values[:,1].astype(str).tolist()

x=data.groupby('year').sum()

s1 = x[x['SKU #4046']==x['SKU #4046'].max()] #Entire row for max SKU #4046

s2 = x[x['SKU #4225']==x['SKU #4225'].max()] #Entire row for max SKU #4225

s3 = x[x['SKU #4770']==x['SKU #4770'].max()] #Entire row for max SKU #4770
