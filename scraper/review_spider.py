import scrapy

class ReviewSpider(scrapy.Spider):
    name = "review_spider"
    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=msi']

    def parse(self, responses):
        SET_SELECTOR = 'a.s-access-detail-page'
        for response in responses.css(SET_SELECTOR):
            yield {
                'name': response.css('h2.a-size-medium::text').extract_first(),
                'link': response.css('::attr(href)').extract_first()
            }