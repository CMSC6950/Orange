# Team Orange

Team Members:

Hanieh Marvikhorasani

Mahesh Kumar Reddy Pochamreddy

Jonathan Conway

---

# Introduction

The growing degree days (GDD) is a temperature index tool used in agriculture to predict the best planting season for a plant. GDD enhances predicting the best planting time of a crop to its maturity, in terms of high heat accumulated in the ground in regions conducive. GDD is used to predict and compare the growing rate of a plant from germination to yielding and predict future planting.
Mathematically, GDD is calculated using the following equation:

begin{equation}
textrm{GDD} = \left(\frac{T_{max} + T_{min}}{2}\right) - T_{base}
label{eqn:gdd}
end{equation}

Generally, GDD is calculated by adding the maximum (Tmax) and minimum (Tmin) temperature together dividing by two (2) and then subtracting the base temperature (Tbase).
When determining the GDD of a plant, each plant has a conducive temperature for development and so it has a base temperature (Tbase). The base temperature is the lowest temperature a plant can survive in. (Tbase) will be considered 5 $^{\circ}$C for the calculation of GDD in this report.
The reference temperature for a given plant is the temperature below which its development slows or stops. For example, peas are planted during the cold season, where it has a reference temperature of 40  $^{\circ}$F while sweet corn and soybeans are planted during the hot season, where they have a reference temperature of 50 degrees  $^{\circ}$F.
In this report, detailed results of GDD calculations will be presented. The GDD calculations were done for three main cities of Canada in 2016 including Victoria, Ottawa, and Montreal.
---

# Methodology
## Data Collection

Required  data  for  different  cities  have  been  obtained  from  the  given  website:
htts://climate.weather.gc.ca.  Also needed columns including year, Min Temp,
Max  Temp  and  etc  have  been  extracted  for  the  selected  cities  and  this  data
have  been  used  to  create  the  plots  for  defined  tasks.   

The main data selected was the monthly data for 2016 from stations located in Montreal, Victoria, and Ottawa. This data was used to complete the required Minimum Core Tasks.

For the regression analysis performed for the Secondary Tasks, data from 1950 to 2010 was selected from a weather station in Montreal.

Data was also selected from unique stations on the island on the Newfoundland based on the 6 different geographic regions. This data spans 10 years and covers the years 1995-2004. This data was used to compile the necessary files for the Final Task analysis which will be elaborated further in this presentation.  

---

## Minimum Core Tasks

1. Downloading the data from the defined url by specific function (”down-
load”) automatically based on station ID, start year and end year.  For
example dowload(5415,1960,2010), downloads weather data for the station 5415 (located in Montreal)
from 1960 to 2010.
---

2. Showing annual cycle of min/max daily temperatures for selected Canadian cities. We did this analysis on Montreal, Victoria, and Ottawa for 2016.

.center[![MinMaxPlot](http://www.cs.mun.ca/~charlesc/cmsc6950/MinMaxPlot.png)]

---

# The Accumulated GDD vs Time Plots

---

# The GitHub Repo

---

# The LaTeX Report
