build:
	g++ greedy.cpp -o greedy

all:
	for f in input_data/*; do ./greedy $$f < $$f > $$(basename $$f); done