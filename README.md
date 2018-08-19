# XKCD Comics Scraper Using Scrapy

## Intro

A Web Scraper that scrapes [XKCD Comics](https://xkcd.com/) using Scrapy. 

## Scraped Contents

* Title
* Whole comic's URL
* Comic image's URL
* Transcript of the comic (if present)

## Requirements

* Python 3.x
* Scrapy

## Usage

    scrapy crawl xkcd-spider > xkcd.json

Example output JSON and HTML source files are [here](./example-output).

## Caveat

Example output has been beautified with [JSON Lint](https://jsonlint.com/) for readability.

Working of this web scraper depends on the source at [XKCD Comics](https://xkcd.com/).

<!-- Foundation for this scraper can be found [here](). -->
