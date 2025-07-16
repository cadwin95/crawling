import os
import re
import argparse
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


def fetch_html(url):
    """Return HTML content of given URL."""
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def extract_article_links(list_url, html):
    """Extract links to article pages from list page HTML."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a['href']
        if re.search(r'selectNttInfo', href):
            links.append(urljoin(list_url, href))
    return links


def extract_image_urls(page_url, html):
    """Extract image URLs from an article page."""
    soup = BeautifulSoup(html, "html.parser")
    images = []
    for img in soup.find_all("img", src=True):
        img_url = urljoin(page_url, img['src'])
        images.append(img_url)
    return images


def download_file(url, dest_folder):
    """Download a single file into destination folder."""
    os.makedirs(dest_folder, exist_ok=True)
    name = os.path.basename(urlparse(url).path)
    if not name:
        name = 'image'
    dest = os.path.join(dest_folder, name)
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(dest, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    return dest


def crawl_images(list_url, output_dir='images'):
    """Crawl all images from a list page and its articles."""
    list_html = fetch_html(list_url)
    article_links = extract_article_links(list_url, list_html)
    image_urls = []
    for link in article_links:
        article_html = fetch_html(link)
        image_urls.extend(extract_image_urls(link, article_html))
    for img_url in image_urls:
        try:
            path = download_file(img_url, output_dir)
            print(f"Downloaded {img_url} -> {path}")
        except Exception as e:
            print(f"Failed {img_url}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Crawl images from a CBE board list page")
    parser.add_argument('url', help='List page URL')
    parser.add_argument('-o', '--output', default='images', help='Output directory for images')
    args = parser.parse_args()
    crawl_images(args.url, args.output)


if __name__ == '__main__':
    main()
