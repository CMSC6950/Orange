#!/usr/bin/env python3

""" Script for creating a plot ehich represents the Minimun GDD for Seed Growth in NL
    this function creates a bar plot of the 10 Year Average Annual GDD for 6 stations on the island of Newfoundland and plots 6 lines for the Minimun GDD for Seed Growth based on research from (http://store.msuextension.org/publications/agandnaturalresources/mt200103ag.pdf)

Args:
    data = pd.read_csv("data/nlinfo.csv", names=['places','gdd']): the imported csv file required to create the plot

Return:
    nlseedplot.png: plot representing the Minimun GDD for Seed Growth in NL based on 6 stations
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
plt.title("Minimun GDD for Seed Growth in NL")
plt.ylabel("10 Year Average Annual GDD (1995-2004)")
#setting the lines for Minimun GDD for Seed Growth
plt.axhline(y=1342, color="yellow", label="Canary")
plt.axhline(y=1603, color="red", label="Flax")
plt.axhline(y=1432, color="green", label="Canola (B. napus)")
plt.axhline(y=1249, color="blue", label="Canola (B. rapa)")
plt.axhline(y=1509, color="orange", label="CMustard (B. juncea)")
plt.axhline(y=1521, color="purple", label="CMustard (S. alba)")
#setting the legend, fixing up the layut, and saving the file
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.savefig('data/nlseedplot.png',index=False)
