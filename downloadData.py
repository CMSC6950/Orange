#!/usr/bin/env python3
import os
import urllib.request
import sys
import pandas as pd

""" Script for downloading data
    this function downloads and then save csv files that have the required columns for our further calculations and plots.
    
Args:
	stationid (int):  this parameter is for the station id of a specific city
	fromYear (int):	  this parameter is for specifying the start year for retrieving the data
	toYear (int) :  this parameter is for specifying the end year for retrieving the data
	
Return:
	string: return a csv file including requested data
"""

def download(stationid,fromYear,toYear):
    data_frame2=[]
    data_frame1=pd.DataFrame()
    if int(fromYear) == int(toYear):
        fname = "{}_{}_t.csv".format(stationid, fromYear)
        url = ("http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(fromYear)+"&Month=8&Day=1&timeframe=2&submit=Download+Data")
        urllib.request.urlretrieve(url, fname)
        data_frame2 = pd.read_csv(fname, skiprows=24, sep=",")
        data_frame1=pd.concat([data_frame2, data_frame1], join='outer')
        os.remove(fname)
    else:
        for year in range(fromYear,toYear+1):
            print(year)
            fname = "{}_{}_t.csv".format(stationid, year)
            url = ("http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data")
            urllib.request.urlretrieve(url, fname)
            data_frame2 = pd.read_csv(fname, skiprows=24, sep=",")
            data_frame1=pd.concat([data_frame2, data_frame1], join='outer')
            os.remove(fname)
    result = data_frame1.iloc[:,[0,1,2,3,5,7]]
    x = str(stationid)
    result.to_csv("docs/temperatures_"+x+".csv", index=False)
    return result

if __name__=="__main__":
    stationId = int(sys.argv[1])
    startYear = int(sys.argv[2])
    endYear = int(sys.argv[3])

    download(stationId, startYear, endYear)
