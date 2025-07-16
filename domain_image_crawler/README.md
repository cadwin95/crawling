# Domain Image Crawler

This folder contains a script to crawl images from any given domain. The
crawler starts from the provided URL, follows internal links and downloads all
images it encounters. Once crawling completes the images are optionally zipped
for easy storage or transfer.

## Setup

Create a virtual environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the crawler with a starting URL. Use `--zip` to store the downloaded images
as a ZIP file.

```bash
python crawler.py https://example.com --zip images.zip
```

Use `--max-pages` to limit how many pages of the domain are visited.
