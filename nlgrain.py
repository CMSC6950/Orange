#!/usr/bin/env python3

import pandas as pd
import matplotlib.pylab as plt
plt.switch_backend('agg')
import csv
import itertools

fnames = ['data/gddvalues_6599.csv','data/gddvalues_6610.csv','data/gddvalues_6633.csv','data/gddvalues_6688.csv','data/gddvalues_6720.csv','data/gddvalues_6743.csv']
placenames = ['Charleston', 'Corner Brook', 'Gander', 'Plum Point', 'St. John\'s', 'Swift Current']

gdd_yearly_sum_all_locations = []
for j in fnames:
    df = pd.read_csv(j, names=['year','gdd'])
    sum_total_place = 0
    gdd_yearly_sum = []
    x = 0
    y = 365
    for i in (list(range(1,11))):
        yearly_sum = sum(df['gdd'].iloc[x:y])
        gdd_yearly_sum.append(yearly_sum)
        if i == 1 or i == 5 or i == 9:
            x = y
            y = y + 366
        else:
            x = y
            y = y + 365
            i =+ 1
    sum_total_place = (sum(gdd_yearly_sum))/10
    gdd_yearly_sum_all_locations.append(sum_total_place)
csvfile = "data/nlinfo.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(zip(placenames, gdd_yearly_sum_all_locations))
