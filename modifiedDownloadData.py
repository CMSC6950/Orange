import os
import urllib.request
import sys
import pandas as pd

def download(stationid, fromYear,toYear):
    print("dowloading data from specified station")
    print("Data of station id {} for year {}".format(stationid, fromYear))
    data_frame2=[]
    data_frame1=pd.DataFrame()
    print(data_frame1)
    for year in range(fromYear,toYear+1):
        fname = "{}_{}_t.csv".format(stationid, year)
        url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
        urllib.request.urlretrieve(url, fname)
        data_frame2 = pd.read_csv(fname, skiprows=24, sep=",")
        data_frame1=pd.concat([data_frame2, data_frame1], join='outer')
        os.remove(fname)
    result = data_frame1[['Date/Time','Year','Month','Day','Max Temp (°C)','Min Temp (°C)']]
    print(result)
    data_frame1.to_csv("temperatures.csv", index=False)
    return result