

.PHONY: all clean web paper presentation

presentation: out/presentation.pdf
	xdg-open $<

web: out/presentation.html
	xdg-open $<

paper: out/paper.pdf
	xdg-open $<


all: presentation web paper

out:
	mkdir -p $@

out/presentation.pdf: apacheSpark.md out
	pandoc -s -t beamer $< -o $@

out/paper.pdf: apacheSpark.md out
	pandoc -s --to=latex $< -o $@

out/presentation.html: apacheSpark.md out
	pandoc -s $< -o $@

clean:
	rm -rf out/*

