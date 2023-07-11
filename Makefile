.PHONY: all clean

all: Coding/data

clean:
	rm -rf Coding/data


Coding/data: archive.zip
	echo "Creating data directory..."
	mkdir -p Coding/data
	cp archive.zip Coding/data/
	unzip Coding/data/archive.zip -d Coding/data/
	rm Coding/data/archive.zip
