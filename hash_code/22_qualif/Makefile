build:
	g++ qualif.cpp -o qualif

all: build
	for f in input_data/*; do echo $$f; ./qualif $$f < $$f > $$(basename $$f); done