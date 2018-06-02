
# coding: utf-8

# In[ ]:


import os
import urllib.request
import sys
import pandas as pd

def download(stationid, year):
    print("Started downloading ...")
    print("Data for station with id {} for year {}".format(stationid, year))
    fname = "{}_{}_t.csv".format(stationid, year)
    url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
    urllib.request.urlretrieve(url, fname)
   
    data_frame2 = pd.read_csv(fname, skiprows=24, sep=",")
    return(data_frame2)

# for runing the code  temporarily use " download(50089, 2015)"


