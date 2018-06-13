import os
import urllib.request
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

colnames=['Year', 'GDD'] 
Gander = pd.read_csv("docs/gddvalues_6633.csv",names=colnames, header=None)


dfGdd=pd.DataFrame()
lyst=[]
yearLyst=[]
lyst.append(Gander.iloc[:365,1].sum())
lyst.append(Gander.iloc[365:731,1].sum())
lyst.append(Gander.iloc[732:1096,1].sum())
lyst.append(Gander.iloc[1096:1461,1].sum())
lyst.append(Gander.iloc[1461:1826,1].sum())
lyst.append(Gander.iloc[1826:2192,1].sum())
lyst.append(Gander.iloc[2192:2557,1].sum())
lyst.append(Gander.iloc[2557:2922,1].sum())
lyst.append(Gander.iloc[2922:3287,1].sum())
lyst.append(Gander.iloc[3287:,1].sum())
idx1=0
idx2=1
yearLyst=[2005,2004,2003,2002,2001,2000,1999,1998,1997,1996]
dfGdd.insert(loc=idx1, column = 'totalGdd', value= lyst)
dfGdd.insert(loc=idx2, column = 'year', value= yearLyst)
sns.regplot(x='year', y='totalGdd', data=dfGdd, order=2, label= 'linear', color='green', marker="+")
plt.title('Annual Growing Degree Days in Gander from 1996 to 2005')
plt.xticks([2005,2004,2003,2002,2001,2000,1999,1998,1997,1996])
plt.savefig('docs/LinReg.png',index=False)
