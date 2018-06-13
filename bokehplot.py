#!/usr/bin/env python3

from bokeh.io import output_file, save
from bokeh.plotting import figure
from bokeh.layouts import column
import pandas as pd

ottawa = pd.read_csv("data/gddvalues_49568.csv", header=None)
montreal = pd.read_csv("data/gddvalues_51157.csv", header=None)
victoria = pd.read_csv("data/gddvalues_51337.csv", header=None)

days=list(range(0,len(ottawa)))

gdd_ottawa =ottawa.iloc[:][1].tolist()
gdd_montreal =montreal.iloc[:][1].tolist()
gdd_victoria =victoria.iloc[:][1].tolist()

ottawaplot = figure(plot_width=1000, plot_height=250, title="GDD for Ottawa in 2016", tools='pan,box_zoom,hover')
ottawaplot.line(days, gdd_ottawa, color='red')

montrealplot = figure(plot_width=1000, plot_height=250, title="GDD for Montreal in 2016", tools='pan,box_zoom,hover')
montrealplot.line(days, gdd_montreal, color='blue')

victoriaplot = figure(plot_width=1000, plot_height=250, title="GDD for Victoria in 2016", tools='pan,box_zoom,hover')
victoriaplot.line(days, gdd_victoria, color='green')

output_file('data/bokehplot.html')

save(column(ottawaplot, montrealplot, victoriaplot))
