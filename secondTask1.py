import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def gddPlot(fromY,toY,stationId) :
    allCsvFiles=glob.glob('gddvalues_'+str(fromY)+'_'+str(toY)+'_'+str(stationId)+'.csv')
    for csv in allCsvFiles:
        fileName=csv
        data_frame2=[]
        data_frame2 = pd.read_csv(csv,sep=",")
        #print(data_frame2)
        data_frame2=clean_data(data_frame2)
        data_frame2.columns = ['Date','GDD']
        gddVal=data_frame2['GDD']
        #print(data_frame2)
        data_frame2 = data_frame2[~data_frame2['Date'].str.endswith('02-29')]
        data_frame2 = data_frame2[~data_frame2['Date'].str.endswith('01-01')]
        fromYear=fileName[10:14]
        toYear=fileName[15:19]
        year=list(range(int(fromYear),int(toYear)+1))
        meanrepl=np.zeros(364)
        for y in year:
            #print(y)
            yearVal=y
            t=data_frame2[data_frame2['Date'].str.contains(str(yearVal)+"-")]
            gddVal=np.array(t['GDD'])
            a = np.array([meanrepl,gddVal])
            meanVal=np.nanmean(a,axis=0)
            meanrepl=meanVal
    
        #print(meanrepl)
        fig = plt.figure(figsize=(10,7))
        ax = fig.add_subplot(111)
        ax.yaxis.grid()
        ax.set_xlabel('Year')
        ax.set_ylabel('Daily Accumulation F')
        x =np.linspace(1,12,len(meanrepl),endpoint=True)
        plt.xticks(np.arange(12),('1-Jan', '1-Feb', '1-Mar', '1-Apr', '1-May', '1-Jun', '1-Jul', '1-Aug', '1-Sep', '1-Oct', '1-Nov', '1-Dec'))
        ax.plot(x,meanrepl,linewidth = 1)
        plt.show()
