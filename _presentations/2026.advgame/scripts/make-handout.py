"""Arrange the existing slides in an edge-to-edge, vector-preserving four-up handout."""

import argparse
from pathlib import Path

import pymupdf


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    with pymupdf.open(args.source) as slides, pymupdf.open() as handout:
        width, height = slides[0].rect.width, slides[0].rect.height
        for first in range(0, len(slides), 4):
            sheet = handout.new_page(width=2 * width, height=2 * height)
            for slot, slide in enumerate(range(first, min(first + 4, len(slides)))):
                row, column = divmod(slot, 2)
                x = column * width
                y = row * height
                sheet.show_pdf_page(
                    pymupdf.Rect(x, y, x + width, y + height), slides, slide
                )
                # show_pdf_page copies the artwork, but not link annotations.
                for link in slides[slide].get_links():
                    if link['kind'] == pymupdf.LINK_URI:
                        sheet.insert_link({
                            'kind': pymupdf.LINK_URI,
                            'from': link['from'] * pymupdf.Matrix(1, 0, 0, 1, x, y),
                            'uri': link['uri'],
                        })
        handout.set_metadata({"title": slides.metadata.get("title", "AdvGame") + " - four-up handout", "author": "Brandon Amos"})
        args.destination.parent.mkdir(parents=True, exist_ok=True)
        handout.save(args.destination, garbage=4, deflate=True)
        print(f"{len(slides)} slides → {len(handout)} handout pages: {args.destination}")


if __name__ == "__main__":
    main()
