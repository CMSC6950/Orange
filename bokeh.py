#!/usr/bin/env python

from bokeh.io import output_file
from bokeh.plotting import figure
import pandas as pd

data = pd.read_csv("docs/gddvalues.csv")

plot = figure(plot_width=400, tools='pan,box_zoom')

plot.circle(data[:,0], data[:,1])

output_file('test.html')

show(plot)
