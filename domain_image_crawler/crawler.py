import argparse
import os
import re
from collections import deque
from urllib.parse import urljoin, urlparse
from zipfile import ZipFile

import requests
from bs4 import BeautifulSoup


def fetch_html(url):
    """Return HTML content of given URL."""
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def extract_links(page_url, html, domain):
    """Extract in-domain links from page HTML."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = urljoin(page_url, a["href"])
        if urlparse(href).netloc == domain:
            links.append(href)
    return links


def extract_image_urls(page_url, html):
    """Extract image URLs from a page."""
    soup = BeautifulSoup(html, "html.parser")
    images = []
    for img in soup.find_all("img", src=True):
        img_url = urljoin(page_url, img["src"])
        images.append(img_url)
    return images


def download_file(url, dest_folder):
    """Download a single file into destination folder."""
    os.makedirs(dest_folder, exist_ok=True)
    name = os.path.basename(urlparse(url).path)
    if not name:
        name = "image"
    dest = os.path.join(dest_folder, name)
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    return dest


def zip_dir(directory, zip_path):
    """Compress directory into a ZIP file."""
    with ZipFile(zip_path, "w") as zf:
        for root, _, files in os.walk(directory):
            for f in files:
                abs_path = os.path.join(root, f)
                arc_name = os.path.relpath(abs_path, directory)
                zf.write(abs_path, arc_name)


def crawl_domain(start_url, output_dir="images", max_pages=10, zip_file=None):
    """Crawl images from pages within the same domain."""
    domain = urlparse(start_url).netloc
    visited = set()
    queue = deque([start_url])
    images = []

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)
        try:
            html = fetch_html(url)
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
            continue
        images.extend(extract_image_urls(url, html))
        for link in extract_links(url, html, domain):
            if link not in visited and len(visited) + len(queue) < max_pages:
                queue.append(link)

    downloaded = []
    for img_url in images:
        try:
            path = download_file(img_url, output_dir)
            downloaded.append(path)
            print(f"Downloaded {img_url} -> {path}")
        except Exception as e:
            print(f"Failed {img_url}: {e}")

    if zip_file:
        zip_dir(output_dir, zip_file)
        print(f"Saved images to {zip_file}")


def main():
    parser = argparse.ArgumentParser(description="Crawl images from a domain")
    parser.add_argument("url", help="Starting URL")
    parser.add_argument("-o", "--output", default="images", help="Output directory")
    parser.add_argument("--zip", help="ZIP file path for downloaded images")
    parser.add_argument("--max-pages", type=int, default=10, help="Maximum pages to visit")
    args = parser.parse_args()

    crawl_domain(args.url, args.output, args.max_pages, args.zip)


if __name__ == "__main__":
    main()
