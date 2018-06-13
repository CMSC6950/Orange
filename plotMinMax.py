#!/usr/bin/env python3

import pandas as pd
import matplotlib.pylab as plt
plt.switch_backend('agg')
import numpy as np
import sys

ottawa = pd.read_csv("data/temperatures_49568.csv")
montreal = pd.read_csv("data/temperatures_51157.csv")
victoria = pd.read_csv("data/temperatures_51337.csv")


lyst=[]
def MinMaxPlot(lyst):
    df = ottawa.iloc[:,[0,1,2,3,4,5]]
    df1= montreal.iloc[:,[0,1,2,3,4,5]]
    df2= victoria.iloc[:,[0,1,2,3,4,5]]

    days=range(0,len(df))
    plt.subplots(figsize=(15,15))


    temp_Max = df.iloc[:,[4]]
    plt.subplot(3,1,1)
    ax2=plt.plot(days, temp_Max,label="Maximum Temp")
    temp_Min= df.iloc[:,[5]]
    ax1=plt.plot(days, temp_Min,label="Minimum Temp")
    plt.xticks([0,30,60,90,120,150,180,210,240,270,300,330,360])
    plt.xlim([0,366])
    ax = plt.gca()
    ax.set_xlabel('Days', fontsize=15)
    ax.set_ylabel('Temperature', fontsize=15)
    plt.title('Annual cycle of Min and Max daily temperatures of '+lyst[0]+' in '+str(lyst[1]), color="black", fontsize=18)
    plt.legend(loc='upper right')
    plt.tight_layout(True)
    plt.grid(True)

    plt.subplot(3,1,2)
    temp_Max1 = df1.iloc[:,[4]]
    temp_Min1= df1.iloc[:,[5]]
    days2 = range(0, len(df1))
    plt.plot(days2, temp_Max1,label="Maximum Temp")
    plt.plot(days2, temp_Min1,label="Minimum Temp")
    ax = plt.gca()
    plt.xlim([0,366])
    plt.xticks([0,30,60,90,120,150,180,210,240,270,300,330,360])
    ax.set_xlabel('Days', fontsize=15)
    ax.set_ylabel('Temperature', fontsize=15)
    plt.title('Annual cycle of Min and Max daily temperatures of '+lyst[2]+' in '+str(lyst[3]), color="black", fontsize=18)
    plt.legend(loc='upper right')
    plt.grid(True)


    plt.subplot(3,1,3)
    temp_Max1 = df2.iloc[:,[4]]
    temp_Min1= df2.iloc[:,[5]]
    days3 = range(0, len(df2))
    plt.plot(days3, temp_Max1,label="Maximum Temp")
    plt.plot(days3, temp_Min1,label="Minimum Temp")
    ax = plt.gca()
    ax.set_xlabel('Days', fontsize=15)
    ax.set_ylabel('Temperature', fontsize=15)
    plt.title('Annual cycle of Min and Max daily temperatures of '+lyst[4]+' in '+str(lyst[5]), color="black", fontsize=18)
    plt.legend(loc='upper right')
    plt.xlim([0,366])
    plt.xticks([0,30,60,90,120,150,180,210,240,270,300,330,360])
    plt.tight_layout()
    plt.grid(True)
    #plt.show()
    plt.savefig('data/MinMaxPlot.png',index=False)

MinMaxPlot(["Montreal",2016,"Ottawa",2016,"Victoria",2016])
