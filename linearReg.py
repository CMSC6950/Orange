import os
import urllib.request
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#read Gdd values for Montreal between 1950 to 2010
Montreal = pd.read_csv("docs/gddvalues_5415.csv", header=None)
Lyst=[]    

#calculating accumulative GDD for each year and appending to a list
for i in range(0,22200,365):
	Lyst.append(Montreal.iloc[i:i+365,1].sum())

dfGdd=pd.DataFrame()
idx1=0
idx2=1
yearLyst=[]
yearLyst=list(range(1950, 2011))
yearLyst2=yearLyst[::-1]

#creating a dataframe and insert two columns: Total Gdd & Year in order to use for making plot
dfGdd.insert(loc=idx1, column = 'Total Gdd', value= Lyst)
dfGdd.insert(loc=idx2, column = 'Year', value= yearLyst2)
#plot regression order2 between year and Total Gdd  
sns.regplot(x='Year', y='Total Gdd', data=dfGdd, order=2, label= 'linear', color='green', marker="+")
plt.title('Annual Growing Degree Days in Montreal from 1950 to 2010')
plt.savefig('docs/LinReg.png',index=False)
