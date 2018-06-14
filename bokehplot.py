#!/usr/bin/env python3

""" Script to create bokeh plot
    this function imports gddvalues data and creates a plot with hover tool capabilities for each import. This file is hardcoded to only import 3 data series.

Args:
	ottawa = pd.read_csv("data/gddvalues_49568.csv", header=None): Import Ottawa GDD Values
    montreal = pd.read_csv("data/gddvalues_51157.csv", header=None): Import Montreal GDD Values
    victoria = pd.read_csv("data/gddvalues_51337.csv", header=None): Import Victoria GDD Values

Return:
    bokehplot.html: HTML document containing the 3 Bokeh Plots
"""

#import required libraries
from bokeh.io import output_file, save
from bokeh.plotting import figure
from bokeh.layouts import column
import pandas as pd
#from datetime import datetime, timedelta

#importing the 3 cities in which the bokeh plot will be created from
ottawa = pd.read_csv("data/gddvalues_49568.csv", header=None)
montreal = pd.read_csv("data/gddvalues_51157.csv", header=None)
victoria = pd.read_csv("data/gddvalues_51337.csv", header=None)

#list of days
days=list(range(0,len(ottawa)))

#attempt at putting actual dates in bokeh
#for day_count in range(0, 366) :
#    curr_date_object = datetime.strptime('2016-01-01', '%Y-%m-%d') + timedelta(days=day_count)
#    print(curr_date_object.strftime("%d %b"))

#creating list from panda dataframe
gdd_ottawa =ottawa.iloc[:][1].tolist()
gdd_montreal =montreal.iloc[:][1].tolist()
gdd_victoria =victoria.iloc[:][1].tolist()

#creating of the plot. hover tool is being set for each plot
ottawaplot = figure(plot_width=1000, plot_height=250, title="GDD for Ottawa in 2016", tools='pan,box_zoom,hover')
ottawaplot.line(days, gdd_ottawa, color='red')

montrealplot = figure(plot_width=1000, plot_height=250, title="GDD for Montreal in 2016", tools='pan,box_zoom,hover')
montrealplot.line(days, gdd_montreal, color='blue')

victoriaplot = figure(plot_width=1000, plot_height=250, title="GDD for Victoria in 2016", tools='pan,box_zoom,hover')
victoriaplot.line(days, gdd_victoria, color='green')

#stacking the 3 plots on top of each other with column and saving the data to an html file
output_file('data/bokehplot.html')
save(column(ottawaplot, montrealplot, victoriaplot))
