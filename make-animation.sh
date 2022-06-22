#!/bin/bash

TMPDIR=/tmp/pres
rm -rf $TMPDIR
mkdir $TMPDIR

for F in *.pdf; do
  convert -density 150 $F -quality 90 -resize 300x200\! \
          $TMPDIR/${F%.pdf}.%03d.png &
done
wait

montage $TMPDIR/*.png -geometry +0+0 -tile 2x2 $TMPDIR/montage.%03d.png
convert -delay 40 $TMPDIR/montage.*.png $TMPDIR/montage.gif
echo "created $TMPDIR/montage.gif"
