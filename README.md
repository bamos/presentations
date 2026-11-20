This repository contains the slides behind [my](http://bamos.github.io) major
presentations with a [CC-BY](http://creativecommons.org/licenses/by/4.0/) license.
The code in here produces the website [here](https://bamos.github.io/presentations/)
to view them.

![](https://user-images.githubusercontent.com/707462/174943502-3e50162b-09a0-4e34-b7c2-c203d8729fce.gif)

## PDF updates

Copy the final slide PDF into `_presentations/` using the filename referenced by
its Markdown entry. Rebuild and visually check the source deck first. Commit the
PDF and any intended entry changes, leaving unrelated local files untouched.

## Montage and video overview

`make-overview.py` produces an all-slide PNG montage and a silent 1080p MP4.
The video shows four slides at a time in reading order, matching the older
animation scripts. Each group stays on screen for one second by default. The
last group is padded with white space, and slide proportions are preserved.

Install the rendering tools on macOS:

```sh
brew install poppler imagemagick ffmpeg
```

Run from this directory, with Python 3:

```sh
python3 make-overview.py _presentations/2026.advgame.pdf \
  ~/tmp/2026.11.19.advgame.mp4
```

This writes `~/tmp/2026.11.19.advgame.mp4` and
`~/tmp/2026.11.19.advgame.montage.png`. Use `--seconds 2` for a slower overview.
The output directory is created if needed; intermediate images use a temporary
directory that is removed after rendering. Existing files at the chosen output
paths are replaced. Keep generated videos and montages outside this repository.
