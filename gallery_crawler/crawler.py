import argparse
import os
import re
from collections import deque
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


DEFAULT_DEPTH = 3


def fetch_html(url: str) -> str:
    """Fetch HTML content of a URL."""
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def extract_links(page_url: str, html: str, domain: str):
    """Return in-domain absolute links from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = urljoin(page_url, a["href"])
        if urlparse(href).netloc == domain:
            links.append(href)
    return links


def extract_image_urls(page_url: str, html: str):
    """Return image URLs from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    images = []
    for img in soup.find_all("img", src=True):
        images.append(urljoin(page_url, img["src"]))
    return images


def looks_like_gallery(url: str, html: str) -> bool:
    """Heuristic to determine if a page is an image gallery."""
    path = urlparse(url).path.lower()
    if re.search(r"gallery|album", path):
        return True
    soup = BeautifulSoup(html, "html.parser")
    return len(soup.find_all("img")) >= 5


def download_file(url: str, dest_folder: str):
    """Download a single file to the given folder."""
    os.makedirs(dest_folder, exist_ok=True)
    name = os.path.basename(urlparse(url).path) or "image"
    dest = os.path.join(dest_folder, name)
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    return dest


def crawl_domain(start_url: str, output_dir: str = "images", max_depth: int = DEFAULT_DEPTH, max_pages: int = 50):
    """Crawl a domain for gallery pages and download their images."""
    domain = urlparse(start_url).netloc
    visited = set()
    queue = deque([(start_url, 0)])

    gallery_pages = []

    while queue and len(visited) < max_pages:
        url, depth = queue.popleft()
        if url in visited or depth > max_depth:
            continue
        visited.add(url)
        try:
            html = fetch_html(url)
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
            continue

        if looks_like_gallery(url, html):
            gallery_pages.append((url, html))

        for link in extract_links(url, html, domain):
            if link not in visited and len(visited) + len(queue) < max_pages:
                queue.append((link, depth + 1))

    for page_url, html in gallery_pages:
        print(f"Processing gallery {page_url}")
        for img_url in extract_image_urls(page_url, html):
            try:
                path = download_file(img_url, output_dir)
                print(f"Downloaded {img_url} -> {path}")
            except Exception as e:
                print(f"Failed {img_url}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Crawl a domain for gallery images")
    parser.add_argument("url", help="Starting URL")
    parser.add_argument("-o", "--output", default="images", help="Output directory")
    parser.add_argument("--max-depth", type=int, default=DEFAULT_DEPTH, help="Maximum link depth")
    parser.add_argument("--max-pages", type=int, default=50, help="Maximum pages to visit")
    args = parser.parse_args()

    crawl_domain(args.url, args.output, args.max_depth, args.max_pages)


if __name__ == "__main__":
    main()
