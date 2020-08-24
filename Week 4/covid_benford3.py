import pandas as pd 
import numpy as np 
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def firstdig(number):
	first_digit = number
	while(first_digit>=10):
		first_digit = first_digit//10
	return first_digit

df = pd.read_csv('covid-all-countries.csv')
#print(df.head())
df['Population'] = df['Population'].fillna(0)
df['Total Deaths'] = df['Total Deaths'].fillna(0)
df['Total Tests'] = df['Total Tests'].fillna(0)


numbers = [float(n) for n in range(1, 10)]
benford = [(math.log10(1 + 1 / d))*100 for d in numbers]
#print(benford)
l = df['Population'][1:198]

cases=[]
for i in df['Population'][1:198]:
	if type(i)==str:
		i=i.replace(',','')
	i = int(i)
	cases.append(firstdig(i))

unique_elements, counts_elements = np.unique(cases, return_counts=True)

new=[]
for i in counts_elements:
	new.append((i/len(l))*100)

#print(np.shape(new))
#print(np.sum(new))
x = [1,2,3,4,5,6,7,8,9]

fig, ax1 = plt.subplots()
ax1.bar(height=new[1:], x = [1,2,3,4,5,6,7,8,9])
ax1.set_ylabel('Population')
ax1.set_xticks(np.arange(len(x)+1))
ax1.set_xlabel('Leading Digit Occurrence %')
ax2 = ax1.twinx()
ax2.plot([1,2,3,4,5,6,7,8,9],benford,color='red')
bottom,top = ax2.get_ylim()
#print(top)
ax1.set_ylim(bottom=0,top=top)
ax2.set_ylim(bottom=0)
plt.show()

population=[]
count =0
for i in df['Total Cases']:
	if type(i)==str:
		i=i.replace(',','')
	i = int(i)
	count = count+i
	population.append(firstdig(i))

unique_elements, counts_elements = np.unique(population, return_counts=True)

new=[]
for i in counts_elements:
	new.append((i/len(df['Total Cases']))*100)

#print(np.shape(new))
#print(np.sum(new))
#print(count)

fig, ax1 = plt.subplots()
#fig.title('Cases')
ax1.bar(height=new, x = [1,2,3,4,5,6,7,8,9])
ax1.set_ylabel('Cases')
ax1.set_xticks(np.arange(len(x)+1))
ax1.set_xlabel('Leading Digit Occurrence %')
ax2 = ax1.twinx()
ax2.plot([1,2,3,4,5,6,7,8,9],benford,color='red')
bottom,top = ax2.get_ylim()
#print(top)
ax1.set_ylim(bottom=0,top=top)
ax2.set_ylim(bottom=0)
plt.show()

deaths=[]
count=0
for i in df['Total Deaths']:
	if type(i)==str:
		i=i.replace(',','')
	i = int(i)
	count = count+i
	deaths.append(firstdig(i))

unique_elements, counts_elements = np.unique(deaths, return_counts=True)

new=[]
for i in counts_elements:
	new.append((i/len(df['Total Deaths']))*100)

#print(np.shape(new))
#print(np.sum(new))
#print(count)

fig, ax1 = plt.subplots()
ax1.bar(height=new[1:], x = [1,2,3,4,5,6,7,8,9])
ax1.set_ylabel('Deaths')
ax1.set_xticks(np.arange(len(x)+1))
ax1.set_xlabel('Leading Digit Occurrence %')
ax2 = ax1.twinx()
ax2.plot([1,2,3,4,5,6,7,8,9],benford,color='red')
bottom,top = ax2.get_ylim()
#print(top)
ax1.set_ylim(bottom=0,top=top)
ax2.set_ylim(bottom=0)
plt.show()

tests=[]
for i in df['Total Tests']:
	if type(i)==str:
		i=i.replace(',','')
	i = int(i)
	tests.append(firstdig(i))

unique_elements, counts_elements = np.unique(tests, return_counts=True)
#print(unique_elements)

new=[]
for i in counts_elements:
	new.append((i/len(df['Total Tests']))*100)

#print(np.shape(new))
#print(np.sum(new))

fig, ax1 = plt.subplots()
ax1.bar(height=new[1:], x = [1,2,3,4,5,6,7,8,9])
ax1.set_xticks(np.arange(len(x)+1))
ax1.set_ylabel('Tests')
ax1.set_xlabel('Leading Digit Occurrence %')
ax2 = ax1.twinx()
ax2.plot([1,2,3,4,5,6,7,8,9],benford,color='red')
bottom,top = ax1.get_ylim()
#print(top)
ax2.set_ylim(bottom=0, top=top)
plt.show()



