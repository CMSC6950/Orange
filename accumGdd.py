#!/usr/bin/env python3

import glob
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import pandas as pd
import sys

""" Script for calculating accumulated Gdd
    this function downloads and then save accumulated Gdd's over period of time
Args:
    stationid (int):  this parameter is for the station id of a specific city
"""
def accGddPlot(stationId) :

    allCsvFiles=glob.glob('data/gddvalues_'+str(stationId)+'.csv')
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
        year=[2010,2015,2016]
        fig = plt.figure(figsize=(10,7))
        ax = fig.add_subplot(111)
        ax.yaxis.grid()
        ax.set_xlabel('Year')
        ax.set_ylabel('cumulative growing degree days(>50°F)')
        avgGdd=[]

        # This is to calculate average temperatures for every day from 1981 to 2010
        years=list(range(int(fromYear),int(2011)))
        meanrepl=np.zeros(364)
        for y in years:
            yearVal=y
            dataFrameVals=data_frame2[data_frame2['Date'].str.contains(str(yearVal)+"-")]
            gddValYears=np.array(dataFrameVals['GDD'])
            a = np.array([meanrepl,gddValYears])
            meanVal=np.nanmean(a,axis=0)
            meanrepl=meanVal

        # Calculates cummulative gdd for 1981 to 2010
        cumdata1=np.cumsum(meanrepl)
        cumdata1=np.array(cumdata1)
        avgGdd.append(cumdata1[len(cumdata1)-1])
        xAx = np.linspace(1,12,len(cumdata1),endpoint=True)
        ax.plot(xAx,cumdata1,label ="1981-2010 Normals",linewidth = 2)

        #This is to calculate cummlative gdd for rest of the years
        for y in year:
            yearVal=y
            t=data_frame2[data_frame2['Date'].str.contains(str(yearVal)+"-")]
            gddVal=np.array(t['GDD'])
            cumdata2=np.cumsum(t['GDD'])
            cumdata2=np.array(cumdata2)
            avgGdd.append(cumdata2[len(cumdata2)-1])
            x = np.linspace(1,12,len(cumdata2),endpoint=True)
            ax.plot(x,cumdata2,label =y,linewidth = 2)

        plt.legend(loc='lower right')
        plt.title("For station :"+str(stationId)+" as of 2016-Growing Degree days comparisions")
        plt.annotate("Cumulative Growing degree days\n"+
               "as of 2016\n"+"1981 -2010 Average = "+str(avgGdd[0])+"\n"
                +"Recent cool year-2010 = "+str(avgGdd[1])+"\n"
             +"Recent warm year-2015 = "+str(avgGdd[2])+"\n"
             +"Current year-2016 = "+str(avgGdd[3])+"\n"
                ,(0.25, 0.8),
                 xycoords="axes fraction", va="center", ha="center",
                 bbox=dict(boxstyle="square, pad=1", fc="w"))
        plt.xticks(np.arange(12),('1-Jan', '1-Feb', '1-Mar', '1-Apr', '1-May', '1-Jun', '1-Jul', '1-Aug', '1-Sep', '1-Oct', '1-Nov', '1-Dec'))
        #filename=str(stationId)+'accGdd.png'
        plt.savefig('data/'+str(stationId)+'accGdd.png',index=False)

def clean_data(dataframe):
#replacing M to NAN in csv data file
    dataframe.replace('E', np.nan,inplace=True)
#replacing M to NAN in csv data file
    dataframe.replace('M', np.nan,inplace=True)
#Then Remove all the 'NAN' data in csv data file
    data = dataframe.dropna(how='any')
    dataframe=data
    return dataframe

if __name__=="__main__":
    stationId = int(sys.argv[1])


    accGddPlot(stationId)
