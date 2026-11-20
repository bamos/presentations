"""Verify the bundled figure assets needed to build the presentation."""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
assets = json.loads((root / 'checks/assets.json').read_text())
missing = [path for path in assets if not (root / path).is_file()]
if missing:
    raise FileNotFoundError('Missing bundled assets: ' + ', '.join(missing))
print(f'Verified {len(assets)} bundled figure assets')
