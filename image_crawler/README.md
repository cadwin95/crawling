# Image Crawler

This folder contains a simple Python script for crawling images from the
[Chungbuk Education Office](https://www.cbe.go.kr) board list. The script
finds all post links on the given list page and then downloads every image
found in those posts.

## Setup

Create a virtual environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the crawler with the URL from the root `README.md`:

```bash
python crawler.py "https://www.cbe.go.kr/news/na/ntt/selectNttList.do?mi=10308&bbsId=1165"
```

Specify an output directory with `-o` to store downloaded images.
