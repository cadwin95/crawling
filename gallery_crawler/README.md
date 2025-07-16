# Gallery Image Crawler

This tool crawls a single domain up to a fixed link depth (default 3) looking
for pages that resemble image galleries. Any images found on those pages are
downloaded to a local folder.

The crawler looks for pages that either contain many images or have "gallery"
or "album" in the URL path.

## Setup

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
python crawler.py https://example.com -o output_folder --max-depth 3
```

Use `--max-pages` to limit the number of total pages visited if needed.
