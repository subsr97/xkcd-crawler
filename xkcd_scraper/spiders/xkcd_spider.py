import scrapy

class xkcdSpider(scrapy.Spider):
    name = "xkcd-spider"
    start_urls = ["https://xkcd.com/1/"]

    def parse(self, response):
        yield {
            'title': response.css("div#ctitle::text").extract_first(),
            'url': response.request.url,
            'img': response.urljoin(response.css("div#comic img::attr(src)").extract_first()),
            'transcript': response.css("div#transcript::text").extract_first(),
        }

        next_page = response.xpath('//a[@rel="next"]/@href').extract_first()

        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)