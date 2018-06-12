TBASE=0
TUPPER=55
DATA_OTTAWA=docs/temperatures_49568.csv
DATA_MONTREAL=docs/temperatures_51157.csv
DATA_VICTORIA=docs/temperatures_51337.csv
DATA_STJOHNS=docs/temperatures_6720.csv
DATA_CHARLESTON=docs/temperatures_6599.csv
DATA_GANDER=docs/temperatures_6633.csv
DATA_CORNER_BROOK=docs/temperatures_6610.csv
DATA_SWIFT_CURRENT=docs/temperatures_6743.csv
DATA_PLUM_POINT=docs/temperatures_6688.csv


#report: plots
	#pdflatex report.tex

#plots: data
	#python make_plots.py

bokehplot: gdd
	./bokehplot.py

gdd: minmaxplot
	./gdd.py $(DATA_OTTAWA) $(TBASE) $(TUPPER)
	./gdd.py $(DATA_MONTREAL) $(TBASE) $(TUPPER)
	./gdd.py $(DATA_VICTORIA) $(TBASE) $(TUPPER)
	./gdd.py $(DATA_STJOHNS) $(TBASE) $(TUPPER)
	./gdd.py $(DATA_CHARLESTON) $(TBASE) $(TUPPER)
	./gdd.py $(DATA_GANDER) $(TBASE) $(TUPPER)
	./gdd.py $(DATA_CORNER_BROOK) $(TBASE) $(TUPPER)
	./gdd.py $(DATA_SWIFT_CURRENT) $(TBASE) $(TUPPER)
	./gdd.py $(DATA_PLUM_POINT) $(TBASE) $(TUPPER)

minmaxplot: dataaquisition
	./plotMinMax.py

dataaquisition: prep
	./downloadData.py

prep:
	mkdir -p docs
	chmod 777 *.*

clean:
	rm -f docs/*.csv
	rm -f docs/*.DS_Store
	rm -f docs/*.png
	rm -f docs/bokehplot.html
	rm -r -f __pycache__
