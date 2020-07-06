#Importing required libraries
import matplotlib
import matplotlib.pyplot as plt
import squarify # pip install squarify (algorithm for treemap)
import pandas as pd
import numpy as np
 
#importing required CSV
df = pd.read_csv("sp-500-index-07-03-2020-mc.csv")
#df.sort_values(by=['Market Cap'],inplace=True,ascending=False)
#print(df['Name'][0:10])

#Creating a list of colours for each of the rectangles in the tree map
colour = []
for i in range(0,20):
	colour.append("#F1C40F")
for i in range(20,506):
	colour.append("#CACFD2")
df['Initialise']=500
#print(df.head)

#Plot depicting S&P 500 companies
sizes = df['Initialise']
labels = df['Symbol']
squarify.plot(sizes=sizes, color=colour,bar_kwargs=dict(linewidth=1, edgecolor="white"))
plt.axis('off')
plt.show()

#Plot depicting S&P 500 companies by market capitalisation
squarify.plot(sizes=df['Market Cap'][:-1], color=colour,text_kwargs={'fontsize':10},bar_kwargs=dict(linewidth=1, edgecolor="white"))
plt.axis('off')
plt.show()

#Calculating weightage of the top 20 companies in the S&P 500 based on market capitalisation
sum1=sum(df['Market Cap'][:-1])
sum2=np.sum(df['Market Cap'][0:19])
for i in range(0,19):
	print(df['Name'].loc[i])
print((sum2/sum1)*100)

