import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
allCsvFiles=glob.glob('gddvalues_*_*_'+str(inutStationId)+'.csv')
AllData=[]
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
#ax = plt.axes()        
ax.yaxis.grid()
ax.set_xlabel('Year')
ax.set_ylabel('cumulative growing degree days(>50°F)')
avgGdd=[]
for csv in allCsvFiles:
    y=csv[10:14]
    data_frame2=[]
    data_frame2 = pd.read_csv(csv,sep=",")
    #print(data_frame2)
    data_frame2=clean_data(data_frame2)
    data_frame2.columns = ['Date','GDD']
    x=data_frame2['Date']
    cumdata2=np.cumsum( data_frame2['GDD'])
    #print(cumdata2[len(cumdata2)-1])
    #avgGdd.append(y)
    avgGdd.append(cumdata2[len(cumdata2)-1])
    x = np.linspace(1,12,len(cumdata2),endpoint=True)
    ax.plot(x,cumdata2,label =y,linewidth = 2)
print(avgGdd)
plt.legend(loc='lower right')
plt.title("St.johns-2017-Growing Degree days comparision(>50°F)")
plt.annotate("Cumulative Growing degree days\n"
                 "as of January 2017\n"+"Recent cool year-2010 = "+str(avgGdd[0])+"\n"
             +"Recent warm year-2015 = "+str(avgGdd[1])+"\n"
             +"Current year-2016 = "+str(avgGdd[2])+"\n"
                ,(0.2, 0.8),
                 xycoords="axes fraction", va="center", ha="center",
                 bbox=dict(boxstyle="square, pad=1", fc="w"))
plt.xticks(np.arange(12),('1-Jan', '1-Feb', '1-Mar', '1-Apr', '1-May', '1-Jun', '1-Jul', '1-Aug', '1-Sep', '1-Oct', '1-Nov', '1-Dec'))
plt.show()
