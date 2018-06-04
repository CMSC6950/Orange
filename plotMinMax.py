import import pandas as pd
import matplotlib.pylab as plt
import numpy as np
from clean-data import clean_data
from downloadData import download

lyst=[]
def MinMaxPlot(lyst):
    #lyst includes 6 values - name of the city and the year for three cities 
    f=download(city_to_stationID(lyst[0]), lyst[1])
    s=download(city_to_stationID(lyst[2]), lyst[3])
    v=download(city_to_stationID(lyst[4]), lyst[5])
    
    
    df = f.iloc[:,[0,1,2,3,5,7,9]]
    df1= s.iloc[:,[0,1,2,3,5,7,9]]
    df2= v.iloc[:,[0,1,2,3,5,7,9]]
    df=clean_data(df)
    df1=clean_data(df1)
    df2=clean_data(df2)
    
    days=range(0,len(df))
    plt.subplots(figsize=(10,7))
    
    temp_Max = df.iloc[:,[4]]
    plt.subplot(3,1,1)
    ax2=plt.plot(days, temp_Max,label="Maximum Temp")
    temp_Min= df.iloc[:,[5]]
    ax1=plt.plot(days, temp_Min,label="Minimum Temp")
    plt.xticks([0,30,60,90,120,150,180,210,240,270,300,330,360]),([r'$Jan$',r'$Feb$',r'$Mar$',r'$Apr$',r'$May$',r'$Jun$',r'$July2$',r'$Aug3$',r'$Sep4$',r'$Oct5$',r'$Nov6$',r'$Dec$'])
    plt.xlim([0,360])
    plt.legend()
        
    plt.subplot(3,1,2)
    temp_Max1 = df1.iloc[:,[4]]
    temp_Min1= df1.iloc[:,[5]]
    days2 = range(0, len(df1))
    plt.plot(days2, temp_Max1,label="Maximum Temp")
    plt.plot(days2, temp_Min1,label="Minimum Temp")
    plt.xticks([0,30,60,90,120,150,180,210,240,270,300,330,360]),([r'$Jan$',r'$Feb$',r'$Mar$',r'$Apr$',r'$May$',r'$Jun$',r'$July2$',r'$Aug3$',r'$Sep4$',r'$Oct5$',r'$Nov6$',r'$Dec$'])
    plt.legend()
    
    plt.subplot(3,1,3)
    temp_Max1 = df2.iloc[:,[4]]
    temp_Min1= df2.iloc[:,[5]]
    days3 = range(0, len(df2))
    plt.plot(days3, temp_Max1,label="Maximum Temp")
    plt.plot(days3, temp_Min1,label="Minimum Temp")
    plt.xticks([0,30,60,90,120,150,180,210,240,270,300,330,360]),([rr'$Jan$',r'$Feb$',r'$Mar$',r'$Apr$',r'$May$',r'$Jun$',r'$July2$',r'$Aug3$',r'$Sep4$',r'$Oct5$',r'$Nov6$',r'$Dec$'])
    plt.legend()
    plt.xlim([0,360])
    plt.tight_layout()
    plt.show()
    #print(len(df)) 
    
