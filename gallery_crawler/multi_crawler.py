import argparse
import os
import re
from pathlib import Path
from urllib.parse import urlparse

from crawler import crawl_domain, DEFAULT_DEPTH

URL_RE = re.compile(r'https?://[^\s)]+')


def load_urls(path: str):
    """Extract all URLs from a text or markdown file."""
    text = Path(path).read_text(encoding="utf-8")
    return [m.group(0) for m in URL_RE.finditer(text)]


def main():
    parser = argparse.ArgumentParser(
        description="Crawl multiple domains listed in a file"
    )
    parser.add_argument(
        "file",
        nargs="?",
        default=os.path.join("..", "docs", "test_sites.md"),
        help="Path to file with URLs (default: docs/test_sites.md)",
    )
    parser.add_argument("-o", "--output", default="sites", help="Base output folder")
    parser.add_argument("--max-depth", type=int, default=DEFAULT_DEPTH)
    parser.add_argument("--max-pages", type=int, default=50)

    args = parser.parse_args()
    urls = load_urls(args.file)
    os.makedirs(args.output, exist_ok=True)

    for url in urls:
        domain = urlparse(url).netloc
        out_dir = os.path.join(args.output, domain)
        print(f"Crawling {url} -> {out_dir}")
        crawl_domain(url, out_dir, args.max_depth, args.max_pages)


if __name__ == "__main__":
    main()
