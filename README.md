This project uses the MIT License. Please refer to LICENSE for further details.

This project is assembled using the Makefile. To run the program, download the repository and run make. You may need to update the permissions on the python scripts. These scripts were tested using the 755 and 777 permission settings.

The first part of the make file creates the data directory. This is created in the Makefile using the PREP target.

Once that is complete, the downloadData.py script is called to download the data from https://climate.weather.gc.ca. This data is publicly available. The downloadData.py script requires 3 arguments, StationID, Start_Year, and End_Year. All 3 inputs are defined in the system command. Each instance of downloadData.py is done using a separate target. The script outputs a temperatures_*.csv file to the data folder.

The gdd.py script is called to calculate the gdd from each temperatures_*.csv file created. The gdd.py script requires 3 arguments, temperatures_*.csv file, TBASE, and TUPPER. TBASE and TUPPER are variables are set in the Makefile and temperatures_*.csv file is defined in the system command and is also set as a dependency. This script outputs a gddvalues_*.csv file to the data folder.

The plotMinMax.py script is called to create the MinMaxPlot.png file. The inputs for this script are hardcoded into the file. The target for this script is MAXMINPLOTS and is a dependency for the ALL target. The dependency of MAXMINPLOTS is TEMPERATURE_ONE_YEAR which is a variable of 3 temperatures_*.csv files created by downloadData.py

The nlgrain.py script is called to calculate the 10 year annual average gdd. The inputs for this file are hardcoded into the script. The target for this script is NLINFO which is a dependency for both NLWHEAT and NLSEED. The dependency for NLINFO is GDD_TEN_YEAR which is a variable of the 6 gddvalues_*.csv calculated for the final task.

The nlseedplot.py script is called to create the plot showing the Minimun GDD for Seed Growth in NL. The inputs for this script are hardcoded into the file. The target for this script is NLSEED and it is a dependency for the ALL target. The dependency of NLSEED is NLINFO which is a variable representing the data/nlinfo.csv file.

The nlwheatplot.py script is called to create the plot showing the Minimun GDD for Wheat Growth in NL. The inputs for this script are hardcoded into the file. The target for this script is NLWHEAT and it is a dependency for the ALL target. The dependency of NLSEED is NLINFO which is a variable representing the data/nlinfo.csv file.

The bokehplot.py script is called to create the bokeh plot. The target for this script is BOKEHPLOT and it is a dependency for the ALL target. The dependency of BOKEHPLOT is GDD_ONE_YEAR and is is a variable containing the gddvalues_*.csv files for the 3 cities. The inputs for this script are hardcoded into the file. The output of this file is bokehplot.html

The linearReg.py script is called to create the linear regression for 60 years worth of Montreal data. This data is gathered using the TEMPERATURE_LONG_MONTREAL, GDD_LONG_MONTREAL variables. The target for this script is MONTREAL_REGRESSION and it is a dependency for the ALL target. The dependency of MONTREAL_REGRESSION is GDD_LONG_MONTREAL and is is a variable containing the data/gddvalues_5415.csv file. The inputs for this script are hardcoded into the file. The output of this file is LinReg.png
