#importing necessary libraries
import pandas as pd 
import numpy as np 
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#function that returns first digit of a number
def firstdig(number):
	first_digit = number
	while(first_digit>=10):
		first_digit = first_digit//10
	return first_digit

#importing csv file and pre-processing
df = pd.read_csv('covid-all-countries.csv')
#print(df.head())
df['Population'] = df['Population'].fillna(0)
df['Total Deaths'] = df['Total Deaths'].fillna(0)
df['Total Tests'] = df['Total Tests'].fillna(0)

#benfords law frequency generator
numbers = [float(n) for n in range(1, 10)]
benford = [(math.log10(1 + 1 / d))*100 for d in numbers]
#print(benford)

#Generating digit frequency occurrence list for Countries Populations
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
x = [1,2,3,4,5,6,7,8,9]

#Plotting Bar graph for Population
fig, ax1 = plt.subplots()
ax1.bar(height=new[1:], x = [1,2,3,4,5,6,7,8,9])
ax1.set_ylabel('Population')
ax1.set_xticks(np.arange(len(x)+1))
ax1.set_xlabel('Leading Digit Occurrence %')
ax2 = ax1.twinx()
ax2.plot([1,2,3,4,5,6,7,8,9],benford,color='red')
bottom,top = ax2.get_ylim()
ax1.set_ylim(bottom=0,top=top)
ax2.set_ylim(bottom=0)
plt.show()


#Generating digit frequency occurrence list for Total Cases in each country
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

#Plotting Bar graph for Test Cases
fig, ax1 = plt.subplots()
ax1.bar(height=new, x = [1,2,3,4,5,6,7,8,9])
ax1.set_ylabel('Cases')
ax1.set_xticks(np.arange(len(x)+1))
ax1.set_xlabel('Leading Digit Occurrence %')
ax2 = ax1.twinx()
ax2.plot([1,2,3,4,5,6,7,8,9],benford,color='red')
bottom,top = ax2.get_ylim()
ax1.set_ylim(bottom=0,top=top)
ax2.set_ylim(bottom=0)
plt.show()

#Generating digit frequency occurrence list for Total Deaths in each country
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

#Plotting Bar graph for COVID-19 Deaths
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

#Generating digit frequency occurrence list for Total Tests in each country
tests=[]
for i in df['Total Tests']:
	if type(i)==str:
		i=i.replace(',','')
	i = int(i)
	tests.append(firstdig(i))

unique_elements, counts_elements = np.unique(tests, return_counts=True)

new=[]
for i in counts_elements:
	new.append((i/len(df['Total Tests']))*100)


#Plotting Bar graph for COVID-19 Tests
fig, ax1 = plt.subplots()
ax1.bar(height=new[1:], x = [1,2,3,4,5,6,7,8,9])
ax1.set_xticks(np.arange(len(x)+1))
ax1.set_ylabel('Tests')
ax1.set_xlabel('Leading Digit Occurrence %')
ax2 = ax1.twinx()
ax2.plot([1,2,3,4,5,6,7,8,9],benford,color='red')
bottom,top = ax1.get_ylim()
ax2.set_ylim(bottom=0, top=top)
plt.show()



