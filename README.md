# crawling

This repository contains several image crawling utilities.

The `image_crawler` script targets the [Chungbuk Education Office](https://www.cbe.go.kr) board:

```
https://www.cbe.go.kr/news/na/ntt/selectNttList.do?mi=10308&bbsId=1165
```

`domain_image_crawler` provides a generic crawler that downloads images from any domain and can save them to a ZIP file.

`gallery_crawler` goes a step further by exploring links up to a configurable depth (default 3) and tries to locate pages that look like image galleries.
It now includes a helper script to crawl every domain listed in `docs/test_sites.md`.

Check each folder's README for setup and usage details.

For a list of recommended websites to test various crawling scenarios, see [docs/test_sites.md](docs/test_sites.md).

`asiad_cc_reservation` demonstrates automating a login and tee time booking on the Asiad CC website. The script uses placeholder URLs that you must adjust to match the real service.
