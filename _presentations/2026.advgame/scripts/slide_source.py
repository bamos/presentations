"""Read the slide assembly without duplicating slide content or notes."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]

def assembled_source():
    source = (ROOT / 'advgame-presentation.tex').read_text()
    return re.sub(r'\\input\{(slides/[^}]+)\}',
                  lambda m: (ROOT / m[1]).read_text().rstrip('\n'), source)

def frame_labels():
    return re.findall(r'\\talkslide\{([^}]+)\}', assembled_source())
