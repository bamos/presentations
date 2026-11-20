#!/usr/bin/env python3
"""Render a PDF as a static montage and a silent 2-by-2 overview video."""

import argparse
import math
from pathlib import Path
import shutil
import subprocess
import tempfile


def run(*args):
    subprocess.run([str(arg) for arg in args], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("video", type=Path, help="Output .mp4 path")
    parser.add_argument("--seconds", type=float, default=1,
                        help="Seconds per four-slide frame (default: 1)")
    args = parser.parse_args()
    if not args.pdf.is_file():
        parser.error("The input PDF does not exist")
    if args.video.suffix.lower() != ".mp4":
        parser.error("The video output must end in .mp4")
    if not math.isfinite(args.seconds) or args.seconds <= 0:
        parser.error("--seconds must be finite and positive")
    for binary in ("pdftoppm", "magick", "ffmpeg"):
        if not shutil.which(binary):
            parser.error(f"Missing {binary}; see README.md for installation")
    args.video.parent.mkdir(parents=True, exist_ok=True)
    montage = args.video.with_suffix(".montage.png")
    with tempfile.TemporaryDirectory(prefix="presentation-overview-") as tmp:
        work = Path(tmp)
        run("pdftoppm", "-scale-to", "960", "-png", args.pdf, work / "slide")
        slides = sorted(work.glob("slide-*.png"),
                        key=lambda p: int(p.stem.rsplit("-", 1)[1]))
        if not slides:
            parser.error("The PDF has no pages")
        # Letterbox without stretching, including non-16:9 source decks.
        for slide in slides:
            run("magick", slide, "-resize", "960x540", "-background", "white",
                "-gravity", "center", "-extent", "960x540", slide)
        blank = work / "blank.png"
        run("magick", "-size", "960x540", "xc:white", blank)
        for frame, start in enumerate(range(0, len(slides), 4)):
            group = slides[start:start + 4]
            group += [blank] * (4 - len(group))
            run("magick", "montage", *group, "-tile", "2x2", "-geometry", "+0+0",
                work / f"frame-{frame:03d}.png")
        run("magick", "montage", *slides, "-thumbnail", "320x180", "-tile", "8x",
            "-geometry", "+3+3", "-background", "#e5e5e5", montage)
        run("ffmpeg", "-hide_banner", "-loglevel", "warning", "-y",
            "-framerate", str(1 / args.seconds), "-i", work / "frame-%03d.png",
            "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-crf", "18",
            "-preset", "medium", "-movflags", "+faststart", "-an", args.video)
    print(f"{len(slides)} slides; {math.ceil(len(slides) / 4)} four-slide frames")
    print(montage)
    print(args.video)


if __name__ == "__main__":
    main()
