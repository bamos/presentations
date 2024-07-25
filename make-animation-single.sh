#!/bin/bash

TMPDIR=/tmp/pres
rm -rf $TMPDIR
mkdir $TMPDIR

F=2024.amortized-optimization-for-OT-and-LLMs.pdf

convert -density 150 $F -quality 90 -resize 600x \
        $TMPDIR/${F%.pdf}.%03d.png

montage $TMPDIR/*.png -geometry +0+0 -tile 2x2 $TMPDIR/montage.%03d.png
convert -delay 100 $TMPDIR/montage.*.png $TMPDIR/montage.gif
echo "created $TMPDIR/montage.gif"
