#!/usr/bin/env python

import argparse
import pandas as pd
import csv

parser = argparse.ArgumentParser()

parser.add_argument('data', action="store", type=str)
parser.add_argument('tbase', action="store", type=int)
parser.add_argument('tupper', action="store", type=int)

args = parser.parse_args()

data = pd.read_csv(args.data)
data = data.fillna(0)

i = 0
gddtable = []
for index, row in data.iterrows():
    gdd = (((data.iloc[i][4] - data.iloc[i][5])/2) - args.tbase)
    if gdd <= 0:
        gdd = 0
    elif gdd >= args.tupper:
        gdd = args.tupper
    gddtable.append(gdd)
    i += 1

time = data.iloc[:,0].tolist()

csvfile = "docs/gddvalues.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(zip(time, gddtable))
