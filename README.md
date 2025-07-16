# crawling

This repository contains image crawling utilities. The original script focuses
on downloading all images from the [Chungbuk Education Office](https://www.cbe.go.kr) board:

```
https://www.cbe.go.kr/news/na/ntt/selectNttList.do?mi=10308&bbsId=1165
```

The code for that crawler resides in the `image_crawler` folder.

A more general crawler that follows links within any domain and stores the
results in a ZIP file is provided in the `domain_image_crawler` folder.
Check each folder's README for setup and usage details.
