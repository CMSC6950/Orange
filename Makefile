TBASE=5
TUPPER=15
DATA_OTTAWA=docs/temperatures_49568.csv
DATA_MONTREAL=docs/temperatures_51157.csv
DATA_VICTORIA=docs/temperatures_51337.csv


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
