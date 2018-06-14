# Team Orange

Team Members:

Hanieh Marvikhorasani

Mahesh Kumar Reddy Pochamreddy

Jonathan Conway

---

# Introduction

The growing degree days (GDD) is a temperature index tool used in agriculture to predict the best planting season for a plant. GDD enhances predicting the best planting time of a crop to its maturity, in terms of high heat accumulated in the ground in regions conducive. GDD is used to predict and compare the growing rate of a plant from germination to yielding and predict future planting. Generally, GDD is calculated by adding the maximum (Tmax) and minimum (Tmin) temperature together dividing by two (2) and then subtracting the base temperature (Tbase).

When determining the GDD of a plant, each plant has a conducive temperature for development and so it has a base temperature (Tbase). The base temperature is the lowest temperature a plant can survive in. (Tbase) will be considered 0 degrees celcius for the calculation of GDD in this report.
The reference temperature for a given plant is the temperature below which its development slows or stops. For example, peas are planted during the cold season, where it has a reference temperature of 40 degrees fahrenheit while sweet corn and soybeans are planted during the hot season, where they have a reference temperature of 50 degrees fahrenheit.
---

#Minimum Core Tasks
##1. Data Collection

Required  data  for  different  cities  have  been  obtained  from  the  given  website:
htts://climate.weather.gc.ca.  Also needed columns including year, Min Temp,
Max  Temp  and  etc  have  been  extracted  for  the  selected  cities  and  this  data
have  been  used  to  create  the  plots  for  defined  tasks.   

---
###1. Data Collection continued

The main data selected was the monthly data for 2016 from stations located in Montreal, Victoria, and Ottawa. This data was used to complete the required Minimum Core Tasks. For the regression analysis performed for the Secondary Tasks, data from 1950 to 2010 was selected from a weather station in Montreal.

.center[<img src="http://www.cs.mun.ca/~charlesc/cmsc6950/Canada_final.jpg">]

---

###1. Data Collection continued

Data was also selected from unique stations on the island on the Newfoundland based on the 6 different geographic regions. This data spans 10 years and covers the years 1995-2004. This data was used to compile the necessary files for the Final Task analysis which will be elaborated further in this presentation.  

---

##2. Showing annual cycle of min/max daily temperatures for selected Canadian cities. We did this analysis on Montreal, Victoria, and Ottawa for 2016.

.center[<img src="http://www.cs.mun.ca/~charlesc/cmsc6950/MinMaxPlot.png" width=400x400]

---

##3. Calculating and storing GDD to analyze via the command line.

The first part of this task was importing the argsparse library which allowed for the passing of command line arguments to the script. Once that was done, a for loop with an if else statement was used to calculate the GDD. If the GDD was less than zero it was set to zero, and if GDD was higher then the user defined upper temperature (tupper), the GDD was set to the value of tupper. This data was then written out to a csv file.

---

##4. Showing accumulated GDD vs time for some selected cities

.center[<img src="http://www.cs.mun.ca/~charlesc/cmsc6950/image_456.png">]

---

##5. Using Git for version control and GitHub for collaboration

Git was used for version control by the team member and allowed the project to be worked on on different platforms and using different software.

GitHub was used as the repository for this project and is where the final files for this project reside.

Our group also faced unique collaboration challenges with team members working opposite schedules and with one team member working from a different province. Tools used for collaboration include face-to-face meetings, phone calls, Skype and BlueJeans Video Conferences, and use of the Slack messaging service.

---

##6. LaTeX report

LaTex was used to make the final report for this project and the Latex file can be found within the docs directory

---

##7. Web based presentation

[This is it!!!! ](https://cmsc6950.github.io/Orange/) Remark js was used to convert a markdown file file into a web slideshow presentation.

---

##8. Makefile

The Makefile is ugly and rudimentary but it works. Variables, targets, and rules are setup to run the project.

---

##10. Documentation

Documentation is provided in each of the python scripts and an overview of how the entire project runs is provided in the README.md file

The License chose for this project was the MIT License with the help of [https://choosealicense.com/](https://choosealicense.com/). "The MIT License is a permissive license that is short and to the point. It lets people do anything they want with your code as long as they provide attribution back to you and don’t hold you liable."

---

#Secondary tasks
##1. Create a plot showing GDD

.center[<img src="http://www.cs.mun.ca/~charlesc/cmsc6950/image_123.png">]

---

##4. Standalone Bokeh Plots

Bokeh was used to make interactive plots. In this case hover point tool is enabled to allow for more information by hovering mouse over a selected point.

[Click Here for Bokeh Plots](http://www.cs.mun.ca/~charlesc/cmsc6950/bokehplot.html)

---

##6. Linear Regression

Data from 1950 to 2010 from a station in Montreal was used to perform Linear Regression on GDD

.center[<img src="http://www.cs.mun.ca/~charlesc/cmsc6950/LinReg.png">]

---

#Final Tasks
For the final task, food security was examined. Food security is a condition related to the availability of food supply. The island of Newfoundland is not known its production of seeds and grain so an analysis was performed to see if solely based on GDD, can different parts of Newfoundland produce seed or grains.

---

The first step was to devide the island of Newfoundland into 6 geographic regions; North, South, East, West, Central, and The Avalon

.center[<img src="http://www.cs.mun.ca/~charlesc/cmsc6950/Island_of_Newfoundland_Regions_final.jpg">]

---

The second step was a station from each region was selected: Plum Point (North), Swift Current (South), Charleston (East), Corner Brook (West), Gander (Central), St. John's (The Avalon)

.center[<img src="http://www.cs.mun.ca/~charlesc/cmsc6950/Island_of_Newfoundland_final.jpg">]

---

Finally, the 10 Year Average Annual GDD was calculated and compared to the minimum GDD for 3 types of wheat. From the analysis, based solely on GDD, parts of Newfoundland could sustain wheat production.

.center[<img src="http://www.cs.mun.ca/~charlesc/cmsc6950/nlwheatplot.png">]

Minimum GDD for wheat production was found [here](http://store.msuextension.org/publications/agandnaturalresources/mt200103ag.pdf)

---

Using the 10 Year Average Annual GDD calculation again, the results were compared to the minimum GDD for 6 types of seeds. From the analysis, based solely on GDD, parts of Newfoundland could sustain wheat production.

.center[<img src="http://www.cs.mun.ca/~charlesc/cmsc6950/nlseedplot.png">]

Minimum GDD for seed production was found [here](http://store.msuextension.org/publications/agandnaturalresources/mt200103ag.pdf)
