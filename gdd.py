#!/usr/bin/env python3

""" Script to finding the gdd date
    this function accepts command line arguments and calculates the gdd based on the temperatures_*.csv file data. The user sets the upper and base temperature values to calculate the gdd values. If the gdd values is less than 0, gdd is set to 0, and if gdd is greate than the user defined upper value, gdd is set to the user defined upper value.

Args:
	date (str): temperatures_*.csv file to be examined
    tbase (int): user defined temperature base
    tupper (int): user defined temperature upper limit

Return:
    gddvalues_*.csv: CSV file with calculated GDD values
"""

#import required libraries
import argparse
import pandas as pd
import csv

#setting argparse to accept command line inputs
parser = argparse.ArgumentParser()
parser.add_argument('data', action="store", type=str)
parser.add_argument('tbase', action="store", type=int)
parser.add_argument('tupper', action="store", type=int)
args = parser.parse_args()

#finding station id
stationid = args.data.split("_")[1]
stationid = stationid.split(".")[0]

#setting data and filling nan values to 0
data = pd.read_csv(args.data)
data = data.fillna(0)

#for loop to loop through each value in the imported csv file
i = 0
gddtable = []
for index, row in data.iterrows():
    gdd = (((data.iloc[i][4] - data.iloc[i][5])/2) - args.tbase)
    #if statement for when gdd is less than 0 or greater user defined temperature upper limit
    if gdd <= 0:
        gdd = 0
    elif gdd >= args.tupper:
        gdd = args.tupper
    gddtable.append(gdd)
    i += 1

#variable for putting time in csv file
time = data.iloc[:,0].tolist()

#writing to csv file
csvfile = "data/gddvalues_"+stationid+".csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(zip(time, gddtable))
