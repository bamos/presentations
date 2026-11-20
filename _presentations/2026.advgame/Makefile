LATEXMK ?= latexmk
PYTHON ?= $(firstword $(wildcard .venv/bin/python) python3)
.PHONY: all assets speaker-notes handout check previews advgame-presentation.pdf speaker-notes.pdf
all: advgame-presentation.pdf speaker-notes.pdf advgame-handout.pdf
assets:
	$(PYTHON) scripts/prepare-assets.py
advgame-presentation.pdf: assets
	nice -n 10 $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error -outdir=build advgame-presentation.tex
	cp build/advgame-presentation.pdf $@
speaker-notes: speaker-notes.pdf
speaker-notes.pdf: advgame-presentation.pdf
	nice -n 10 $(LATEXMK) -pdf -jobname=speaker-notes -usepretex='\def\speakerscript{1}' -interaction=nonstopmode -halt-on-error -outdir=build advgame-presentation.tex
	cp build/speaker-notes.pdf $@
handout: advgame-handout.pdf
advgame-handout.pdf: advgame-presentation.pdf scripts/make-handout.py
	$(PYTHON) scripts/make-handout.py advgame-presentation.pdf advgame-handout.pdf
check: all
	$(PYTHON) scripts/check-deck.py
previews: all
	$(PYTHON) scripts/render-review.py

.PHONY: preview
preview:
	$(PYTHON) scripts/preview-slide.py $(SLIDE)
