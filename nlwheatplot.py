#!/usr/bin/env python3

""" Script for creating a plot ehich represents the Minimun GDD for Wheat Growth in NL
    this function creates a bar plot of the 10 Year Average Annual GDD for 6 stations on the island of Newfoundland and plots 6 lines for the Minimun GDD for Wheat Growth based on research from (http://store.msuextension.org/publications/agandnaturalresources/mt200103ag.pdf)

Args:
    data = pd.read_csv("data/nlinfo.csv", names=['places','gdd']): the imported csv file required to create the plot

Return:
    nlwheatplot.png: plot representing the Minimun GDD for wheat Growth in NL based on 6 stations
"""

#import required libraries
import pandas as pd
import matplotlib.pylab as plt
plt.switch_backend('agg')

#importing data
data = pd.read_csv("data/nlinfo.csv", names=['places','gdd'])

#creating the bar graph and setting the labels
plt.bar(data['places'], data['gdd'], color='grey')
plt.xticks(rotation=45)
plt.title("Minimun GDD for Wheat Growth in NL")
plt.ylabel("10 Year Average Annual GDD 1995-2004)")
#setting the lines for Minimun GDD for Wheat Growth
plt.axhline(y=1269, color="blue", label="Barley")
plt.axhline(y=1538, color="red", label="Wheat (Hard Red)")
plt.axhline(y=1483, color="green", label="Oat")
#setting the legend, fixing up the layut, and saving the file
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.savefig('data/nlwheatplot.png',index=False)
