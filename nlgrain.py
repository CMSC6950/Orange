#!/usr/bin/env python3

import pandas as pd

swift_current_gdd = pd.read_csv("docs/gddvalues_6743.csv", header=None)

#year1 = swift_current_gdd.iloc[:365][1]
#year2 = swift_current_gdd.iloc[365:731][1]
#year3 = swift_current_gdd.iloc[731:1096][1]
#year4 = swift_current_gdd.iloc[1096:1461][1]
#year5 = swift_current_gdd.iloc[1461:1826][1]
#year6 = swift_current_gdd.iloc[1826:2192][1]
#year7 = swift_current_gdd.iloc[2192:2557][1]
#year8 = swift_current_gdd.iloc[2557:2922][1]
#year9 = swift_current_gdd.iloc[2922:3287][1]
#year10 = swift_current_gdd.iloc[3287:][1]

places = ['swift_current_gdd']

gdd_yearly_sum_all_locations = []
for j in places["j"]:
    sum_total_place = 0
    gdd_yearly_sum = []
    x = 0
    y = 365
    for i in (list(range(1,11))):
        yearly_sum = sum(places[j].iloc[x:y][1])
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
print(gdd_yearly_sum_all_locations)
