dir=fb_hacker_cup/2021/round2/B
pw=2893ba22a1845615cb1aed684a7193e1

solve:
	cd $(dir); \
	rm -f output test *.txt; \
	7z e *.zip -P$(pw); \
	(python3 *.py < $$(echo *.txt)) > output

test:
	cd $(dir); \
	rm -f test; \
	python3 *.py < $$(echo *.txt) > test
