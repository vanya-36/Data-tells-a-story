#importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#function to compute standard/z-score
def std_score(col):
	m = df[col].mean()
	sd = df[col].std()
	#print(m,sd)
	#print(df[col].max(),df[col].min())
	df[col+' Std score'] = 0
	for i in range(np.shape(df)[0]):
		df[col+' Std score'].loc[i] = (df[col].loc[i]-m)/sd

#importing CSV and preprocessing
df = pd.read_csv('sp-500-index-07-03-2020-mc-csv-employees-edit.csv')
df=df[:-1]

cols = ['Unnamed: 0', 'Symbol', 'Last', 'Change', '%Chg', 'High', 'Low','Volume', 'Time',  'Unnamed: 10', '3 months ago','Unnamed: 12',]
df.drop(columns=cols,inplace=True)
std_score('Market Cap')
std_score('Employees')
#print(df['Market Cap'],df['Employees'])
#print(df['Market Cap Std score'].loc[9],df['Employees Std score'].loc[9])
df['Market Cap Std score'].loc[9]=0
df['Employees Std score'].loc[9]=0

#variables for plotting 
c = range(np.shape(df)[0])
fig, ax = plt.subplots()
ax.set(xlabel = "Market Cap Std score", ylabel = "Employees Std score")

#plotting crosshairs
plt.xlim(df['Market Cap Std score'].min()-1,df['Market Cap Std score'].max()+1)
plt.ylim(df['Employees Std score'].min()-1,df['Employees Std score'].max()+1)
#print(df['Market Cap Std score'].min(),df['Market Cap Std score'].max())
plt.plot([-1,11],[3,3],'k-', linestyle = ":", lw=1)
plt.plot([5,5],[-1,11],'k-', linestyle = ":", lw=1)

#scatterplot
sc = plt.scatter(df['Market Cap Std score'],df['Employees Std score'])

#code for annotating points on the plot and enabling hover
annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):

    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                           " ".join([df['Name'].loc[n] for n in ind["ind"]]))
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()
                
#plotting the figure with annotations
fig.canvas.mpl_connect("motion_notify_event", hover)
plt.show()
