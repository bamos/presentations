#!/usr/bin/env python3
"""Validate file references inside post front matter."""
from __future__ import annotations

from collections import defaultdict
import re
import socket
import sys
from pathlib import Path
from typing import Iterable, Tuple
from urllib.parse import urlparse
from urllib import error as url_error
from urllib import request as url_request

try:  # Prefer PyYAML when available, fall back otherwise.
    import yaml  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - PyYAML optional
    yaml = None

ROOT = Path(__file__).resolve().parent
POSTS_DIR = ROOT / "_posts"
FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*", re.DOTALL)
URL_PATTERN = re.compile(r"https?://[^\s)\]>]+", re.IGNORECASE)
URL_TIMEOUT = 10
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) "
        "Gecko/20100101 Firefox/133.0"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def looks_like_url(value: str) -> bool:
    parsed = urlparse(value)
    return bool(parsed.scheme and parsed.netloc)


def looks_like_file(value: str) -> bool:
    candidate = value.strip()
    if not candidate:
        return False
    if any(ch.isspace() for ch in candidate):
        return False
    if looks_like_url(candidate):
        return False
    if candidate.startswith("#"):
        return False
    return "." in candidate or "/" in candidate


def iter_strings(value) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, (list, tuple, set)):
        for item in value:
            yield from iter_strings(item)


def parse_front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        raise ValueError("missing YAML front matter")
    raw = match.group(1)

    if yaml is not None:
        data = yaml.safe_load(raw) or {}
        if not isinstance(data, dict):
            raise ValueError("front matter is not a mapping")
        return data

    return _parse_simple_yaml(raw)


def extract_urls(value: str) -> list[str]:
    urls = []
    for match in URL_PATTERN.findall(value):
        cleaned = match.rstrip(".,);]")
        urls.append(cleaned)
    return urls


def check_url_target(url: str) -> Tuple[bool, str]:
    for method in ("HEAD", "GET"):
        try:
            req = url_request.Request(url, method=method, headers=DEFAULT_HEADERS)
            with url_request.urlopen(req, timeout=URL_TIMEOUT) as resp:
                status = getattr(resp, "status", getattr(resp, "code", None))
                if status is None:
                    return True, "reachable"
                if 200 <= status < 400:
                    return True, f"HTTP {status}"
                return False, f"HTTP {status}"
        except url_error.HTTPError as exc:
            status = getattr(exc, "code", None)
            if status == 405 and method == "HEAD":
                continue
            if status is not None:
                return False, f"HTTP {status}"
            return False, "HTTP error"
        except url_error.URLError as exc:
            reason = exc.reason
            if isinstance(reason, socket.timeout):
                return False, "timeout"
            if isinstance(reason, socket.gaierror):
                return False, "DNS lookup failed"
            return False, str(reason)
    return False, "unknown error"


def _parse_simple_yaml(raw: str):
    data = {}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.lstrip() != line:
            # Continuation line without a preceding block indicator.
            raise ValueError("unexpected indentation without block indicator")
        if ':' not in line:
            raise ValueError(f"unable to parse line: {line}")
        key, raw_value = line.split(':', 1)
        key = key.strip()
        value = raw_value.lstrip()

        if value in {'>-', '>|', '>', '|', '|-', '>-' }:
            block_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i]
                if not next_line.strip():
                    block_lines.append('')
                    i += 1
                    continue
                if next_line.startswith(' '):
                    block_lines.append(next_line.lstrip())
                    i += 1
                    continue
                break
            data[key] = '\n'.join(block_lines).strip()
            continue

        if value.startswith('[') and value.endswith(']'):
            inner = value[1:-1].strip()
            data[key] = [item.strip().strip("'\"") for item in inner.split(',') if item.strip()]
        elif (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            data[key] = value[1:-1]
        else:
            data[key] = value
        i += 1

    return data


def main() -> int:
    errors = defaultdict(list)
    checked = 0
    posts_checked = 0

    for post in sorted(POSTS_DIR.glob("*")):
        if not post.is_file():
            continue
        posts_checked += 1
        rel_post = post.relative_to(ROOT)
        try:
            data = parse_front_matter(post)
        except Exception as exc:  # pylint: disable=broad-except
            errors[str(rel_post)].append(f"front-matter --- {exc}")
            continue

        for key, value in data.items():
            for entry in iter_strings(value):
                if not isinstance(entry, str):
                    continue
                clean_entry = entry.strip()

                url_targets = set(extract_urls(clean_entry))
                if looks_like_url(clean_entry):
                    url_targets.add(clean_entry)

                for target_url in url_targets:
                    ok, info = check_url_target(target_url)
                    if not ok:
                        errors[str(rel_post)].append(
                            f"{key}: {target_url} --- {info}"
                        )
                    checked += 1

                if looks_like_file(clean_entry):
                    target = (ROOT / clean_entry).resolve()
                    # ensure the path stays within repo root
                    try:
                        target.relative_to(ROOT)
                    except ValueError:
                        errors[str(rel_post)].append(
                            f"{key}: {clean_entry} --- outside repository"
                        )
                        checked += 1
                        continue
                    if not target.exists():
                        errors[str(rel_post)].append(
                            f"{key}: {clean_entry} --- not found"
                        )
                    checked += 1

    if errors:
        total_posts = len(errors)
        total_issues = sum(len(items) for items in errors.values())
        lines = []
        for post in sorted(errors):
            lines.append(f"=== {post}")
            for issue in errors[post]:
                lines.append(issue)
        print("\n".join(lines), file=sys.stderr)
        return 1

    print(f"Checked {checked} references across {posts_checked} posts; all exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
