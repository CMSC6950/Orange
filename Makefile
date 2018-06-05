TBASE=10
TUPPER=20
STATIONID=1998
YEAR=2000


#report: plots
	#pdflatex report.tex

#plots: data
	#python make_plots.py

#data: prep

prep:
	./gdd.py $(TBASE) $(TUPPER) $(YEAR)

clean:
