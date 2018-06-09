TBASE=10
TUPPER=20
DATA=docs/temperatures.csv


#report: plots
	#pdflatex report.tex

#plots: data
	#python make_plots.py


gdd: dataaquisition
	./gdd.py $(DATA) $(TBASE) $(TUPPER)

dataaquisition: prep
	./downloadData.py

prep:
	mkdir -p docs
	chmod 777 *.*

clean:
	rm -f docs/*.csv
	rm -f docs/*.DS_Store
