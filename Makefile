TBASE=0
TUPPER=55

DATA_LONG_MONTREAL=docs/temperatures_5415.csv

DATA_OTTAWA=docs/temperatures_49568.csv
DATA_MONTREAL=docs/temperatures_51157.csv
DATA_VICTORIA=docs/temperatures_51337.csv
ONE_YEAR = $(DATA_OTTAWA) $(DATA_MONTREAL) $(DATA_VICTORIA)

DATA_STJOHNS=docs/temperatures_6720.csv
DATA_CHARLESTON=docs/temperatures_6599.csv
DATA_GANDER=docs/temperatures_6633.csv
DATA_CORNER_BROOK=docs/temperatures_6610.csv
DATA_SWIFT_CURRENT=docs/temperatures_6743.csv
DATA_PLUM_POINT=docs/temperatures_6688.csv
TEN_YEAR = $(DATA_STJOHNS) $(DATA_CHARLESTON)
DATA_FILES=$(ONE_YEAR) $(TEN_YEAR) $(DATA_LONG_MONTREAL)

# Idea for the future...
#GDD_FILES = $(prefix $(DATA_FILES),gddvalues_)

DATA=docs/nlinfo.csv
PLOTS=docs/MaxMinPlot.png,

ALL: $(PLOTS) $(DATA_LONG_MONTREAL) $(DATA)

#report: $(PLOTS)
	#pdflatex report.tex

#plots: data
	#python make_plots.py

#bokehplot: gdd
#	./bokehplot.py

$(DATA): docs/gddvalues_%.csv
	./nlgrain.py

docs/gddvalues_%.csv: docs/temperatures_%.csv
	./gdd_py $^ $(TBASE) $(TUPPER)

$(PLOTS): $(ONE_YEAR)
	./plotMinMax.py $@

$(DATA_LONG_MONTREAL):
	python ./downloadData.py 5415 1950 2010

docs/temperatures_%.csv:
	python ./downloadData.py $* \
		$(if $(findstring $@,$(TEN_YEAR)),2016,2016) \
		$(if $(findstring $@,$(ONE_YEAR)),2015,2016) \

prep:
	chmod 755 *.*

clean:
	rm -f docs/*.csv
	rm -f docs/*.DS_Store
	rm -f docs/*.png
	rm -f docs/bokehplot.html
	rm -r -f __pycache__
