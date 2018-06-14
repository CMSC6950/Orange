import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def gddPlot(stationId) :
    
    allCsvFiles=glob.glob('gddvalues_'+str(stationId)+'.csv')
    for csv in allCsvFiles:
        fileName=csv
        data_frame2=[]
        data_frame2 = pd.read_csv(csv,sep=",")
        data_frame2=clean_data(data_frame2)
        data_frame2.columns = ['Date','GDD']
        gddVal=data_frame2['GDD']
        datesAll=np.array(data_frame2['Date'])
        x=np.frompyfunc(lambda x:x[0:4],1,1)(datesAll)
        x=np.sort(x)
        data_frame2 = data_frame2[~data_frame2['Date'].str.endswith('02-29')]
        data_frame2 = data_frame2[~data_frame2['Date'].str.endswith('01-01')]
        fromYear=x[0]
        toYear=x[-1]
        year=list(range(int(fromYear),int(toYear)+1))
        meanrepl=np.zeros(364)
        for y in year:
            #print(y)
            yearVal=y
            t=data_frame2[data_frame2['Date'].str.contains(str(yearVal)+"-")]
            gddVal=np.array(t['GDD'])
            #print(gddVal)
            a = np.array([meanrepl,gddVal])
            meanVal=np.nanmean(a,axis=0)
            meanrepl=meanVal
        fig = plt.figure(figsize=(20,20))
        ax = fig.add_subplot(111)
        
        ax.yaxis.grid()
        ax.set_xlabel('Time')
        ax.set_ylabel('Daily Accumulation (Celicius)')
        x =np.linspace(1,12,len(meanrepl),endpoint=True)
        plt.xticks(np.arange(12),('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
        #print(meanrepl)
        ax.plot(x,meanrepl,linewidth = 1,color="red",label='Average')
        upper1=np.array(meanrepl)*(95/100)*2
        upper2=np.array(meanrepl)*(75/100)*2
        lower1=np.array(meanrepl)*(5/100)*2
        lower2=np.array(meanrepl)*(25/100)*2
        ax.set_title(str(fromYear)+'-'+str(toYear) +' daily Growing degree days of '+str(stationId))
        ax.fill_between(x,lower1,upper1,alpha=0.3,color="blue", label="5-95 percentile")
        ax.fill_between(x,lower2,upper2,alpha=0.3,color="yellow",label="25-75 percentile")
        scatterData=data_frame2[data_frame2['Date'].str.contains(str(toYear)+"-")]
        scatGdd=np.array(scatterData['GDD'])
        ax.scatter(x,scatGdd,alpha=0.7,color='black',label=toYear)
        plt.legend(loc='upper right',)
        plt.show()
gddPlot(3932)
