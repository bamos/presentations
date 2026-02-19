#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp $SCRIPT_DIR/Cambria_orig.ttc /Applications/Microsoft\ PowerPoint.app/Contents/Resources/DFonts/Cambria.ttc
