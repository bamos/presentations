# AdvGame presentation

Beamer source for **AdvGame: Safety Alignment of LMs via Non-cooperative Games**
(ICML 2026), presented at the Penn ASSET Center Seminar

[Presentation and PDF](https://bamos.github.io/presentations/2026.advgame.html)
· [Research code](https://github.com/facebookresearch/advgame)

## Build

Install a LaTeX distribution with `pdflatex` and `latexmk` (such as TeX Live or
MacTeX), and Python 3. From this directory:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
make
```

The default target creates the slides, speaker notes, and four-slide handout:

- `advgame-presentation.pdf`
- `speaker-notes.pdf`
- `advgame-handout.pdf`

These generated files are ignored by Git. The published PDF stays at
[`../2026.advgame.pdf`](../2026.advgame.pdf). The PDFs bundled in `assets/` and
`figures/` are figure dependencies. No other repository checkout is required
to build the presentation.

## Source structure

- `advgame-presentation.tex` assembles the deck and its notes
- `slides/` contains one file per slide, including its `\speak{...}` notes
- `figures/` contains shared diagrams, plots, and figure data
- `styles/` contains the theme, title layout, portraits, and reference formatting
- `assets/` contains images and imported vector figures
- `scripts/` contains build, preview, and validation helpers
- `checks/` records slide order, required assets, and expected numerical results

Builds are explicit slides rather than Beamer overlays. Shared diagrams keep
their geometry consistent between successive slides.

## Check and preview

```sh
make check
```

This checks slide order, numerical results, notes and handout coverage, text
bounds, and build warnings. It supplements visual inspection of the rendered
slides.

Install Poppler for PNG previews (`brew install poppler` on macOS). Preview a
slide using its filename without `.tex`:

```sh
make preview SLIDE=attacker-loss
make preview SLIDE='title thanks'
```

The previews use the full theme and fonts and are written to
`build/slide-previews/`. To render all slides, notes, and handout pages:

```sh
make previews
```

These images and contact sheets are written to `previews/` and are ignored by Git.
