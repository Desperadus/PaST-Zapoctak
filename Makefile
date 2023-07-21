.PHONY: all clean

all: Coding/data main.pdf Coding/corr_matrix.pdf Coding/genders_mean_suicide_rate.pdf Coding/happiness_and_rates.pdf

clean:
	rm -rf Coding/data
	rm -f Latex/main.pdf
	rm -f result.pdf
	rm -f Coding/*.pdf
	rm -f *.pdf
	rm -f Latex/*.pdf


Coding/data: archive.zip happiness.zip gdp.zip
	echo "Creating data directory..."
	mkdir -p Coding/data
	cp archive.zip Coding/data/
	unzip Coding/data/archive.zip -d Coding/data/
	rm Coding/data/archive.zip
	cp happiness.zip Coding/data/
	unzip Coding/data/happiness.zip -d Coding/data/
	rm Coding/data/happiness.zip
	cp gdp.zip Coding/data/
	unzip Coding/data/gdp.zip -d Coding/data/
	rm Coding/data/gdp.zip
	sed -i 's/Country Name/Country/g' Coding/data/gdp*.csv

main.pdf: Latex/main.tex Latex/citations.bib Coding/data Coding/male_and_female.py Coding/genders_mean_suicide_rate.pdf
	echo "Creating Latex/main.pdf..."
	cd Latex && pdflatex main.tex > /dev/null && cp main.pdf ../result.pdf && rm main.pdf

Coding/genders_mean_suicide_rate.pdf Coding/corr_matrix.pdf Coding/happiness_and_rates.pdf: Coding/make_pdf_plots.py 
	cd Coding && python3 make_pdf_plots.py
