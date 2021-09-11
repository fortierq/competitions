dir=fb_hacker_cup/2021/round1
pw=259d69efcd9df06101442e412f15b547

solve:
	cd $(dir); \
	7z e *.zip -P$(pw); \
	input_txt=$(input); \
	(python3 *.py < $$(echo *.txt)) > output
