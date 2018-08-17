Py=$(shell ls *.py)
Md=$(Py:.py=.md)

all: $(Md)

%.md : %.py
	@gawk -f make.awk $< > $@

eg1: $(Md)
	@python3 w1.py
