#!/usr/bin/env python3

''' This is Secondory Task 1:'''
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

""" Script for calculating accumulated Gdd
    this function downloads and then save Average Gdd's over period of time
Args:
    stationid (int):  this parameter is for the station id of a specific city
"""

def gddPlot(stationId) :
    ''' This Function calculates mean gdd temperatures of every day over given period of time for particular station Id.
    To this function input is station Id. Along with this,scatter plot for current year also calculated'''
    
    allCsvFiles=glob.glob('gddvalues_'+str(stationId)+'.csv')
    #This for loop is to calculate mean temperatures for every csv input file
    for csv in allCsvFiles:
        fileName=csv 
        data_frame2=[]
        data_frame2 = pd.read_csv(csv,sep=",") #Reads csv to dataframe
        data_frame2=clean_data(data_frame2)
        data_frame2.columns = ['Date','GDD']
        gddVal=data_frame2['GDD']
        datesAll=np.array(data_frame2['Date']) #Creating np array for all gdd values
        x=np.frompyfunc(lambda x:x[0:4],1,1)(datesAll) #This is to slice year from the Date column
        x=np.sort(x)  
        data_frame2 = data_frame2[~data_frame2['Date'].str.endswith('02-29')] # Excluding Feb 29th gdd values
        data_frame2 = data_frame2[~data_frame2['Date'].str.endswith('01-01')]
        fromYear=x[0]
        toYear=x[-1]
        year=list(range(int(fromYear),int(toYear)+1))
        divVal=np.abs(int(toYear)-int(fromYear))
        meanrepl=np.zeros(364)
        
        # This loop is to calculate gdd mean by looping thru every year 
        for y in year:
            yearVal=y
            t=data_frame2[data_frame2['Date'].str.contains(str(yearVal)+"-")]
            gddVal=np.array(t['GDD'])
            a=np.add(meanrepl,gddVal)
            meanrepl=a
        
        meanrepl=np.array(meanrepl)
        meanrepl=meanrepl/(divVal)
        fig = plt.figure(figsize=(20,20))
        ax = fig.add_subplot(111)
        
        ax.yaxis.grid()
        ax.set_xlabel('Time')
        ax.set_ylabel('Daily Accumulation (Celicius)')
        x =np.linspace(1,12,len(meanrepl),endpoint=True)
        plt.xticks(np.arange(12),('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
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
        plt.savefig('data/SecondTask1.png',index=False) 

if __name__=="__main__":
    stationId = int(sys.argv[1])
    

    gddPlot(stationId)        
        
