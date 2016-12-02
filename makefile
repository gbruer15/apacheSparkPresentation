

.PHONY: all clean

all: out/presentation.pdf

out:
	mkdir -p $@

out/presentation.pdf: apacheSpark.md out
	pandoc -s --to=latex $< -o $@
	xdg-open $@

out/presentation.html: apacheSpark.md out
	pandoc -s --to=latex $< -o $@
	xdg-open $@


clean:
	rm -rf out/*

