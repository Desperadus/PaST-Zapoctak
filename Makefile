.PHONY: all clean

all: Coding/data Latex/main.pdf

clean:
	rm -rf Coding/data


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

Latex/main.pdf: Latex/main.tex Latex/citations.bib Coding/data Coding/male_and_female.py Coding/genders_mean_suicide_rate.pdf
	echo "Creating Latex/main.pdf..."
	cd Latex && pdflatex -pdf main.tex && ln -s main.pdf ../result.pdf

Coding/genders_mean_suicide_rate.pdf: Coding/make_pdf_plots.py 
