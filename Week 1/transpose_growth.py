#Required libraries
import pandas as pd
import numpy as np
import math

#Function that calculates and returns growth percentage
def growth_func(a,b):
	g = (a-b)/a
	g = g*100
	return g

#Importing and pre-processing the S&P 500 CSV
df = pd.read_csv("S&P500_monthly.csv")
#print(df.shape)
df['S&P Growth']=""
df['Trade Vol Growth']=""

#Calculating growth of S&P 500 index
for i in range(1,np.shape(df)[0]-1):
	df['S&P Growth'].loc[i+1]=growth_func(df['Close'].loc[i+1],df['Close'].loc[i])
	df['Trade Vol Growth'].loc[i+1]=growth_func(df['Volume'].loc[i+1],df['Volume'].loc[i])
#print(df.head)

#Importing and pre-processing the Gold Monthly Average CSV
df1 = pd.read_csv("Gold_Monthly_Average.csv")
#print(df1.head)
df1['Gold Growth']=""
df1['Gold Price']=""

#Calculating growth of Gold Prices
for i in range(1,np.shape(df1)[0]-1):
	if ',' in df1['US dollar'].loc[i+1]:
		df1['US dollar'].loc[i+1]=df1['US dollar'].loc[i+1].replace(',', '')
	if ',' in df1['US dollar'].loc[i]:
		df1['US dollar'].loc[i]=df1['US dollar'].loc[i].replace(',', '')
	df1['Gold Growth'].loc[i+1]=growth_func(float(df1['US dollar'].loc[i+1]),float(df1['US dollar'].loc[i]))
print(df1.head)


#Some additional processing
df2 = df.transpose()
df5=df.transpose()
df3 = df1.transpose()
#print(df3.head)
req_row = df3.iloc[25]
#print(req_row)
df2.loc[7]=req_row
df2.loc[7][0]='Gold Growth'
df4 = df2.transpose()

#Saving the processed CSVs for further plotting and analysis
df.to_csv("S&P500_monthly_growth_with_tvol_cols.csv")
df2.to_csv("Gold_US_S&P500_monthly_growth.csv")
df4.to_csv("Gold_US_S&P500_monthly_growth_cols.csv")
df5.to_csv("S&P500_monthly_growth_with_tvol.csv")

