#!/usr/bin/env python3
import os
import urllib.request
import sys
import pandas as pd

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

download(51157, 2016, 2016)
download(49568, 2016, 2016)
download(51337, 2016, 2016)
download(6720, 1996, 2005)
download(6599, 1996, 2005)
download(6633, 1996, 2005)
download(6610, 1996, 2005)
download(6743, 1996, 2005)
download(6688, 1996, 2005)
