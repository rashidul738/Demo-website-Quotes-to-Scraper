import scrapy


class ScrapSpider(scrapy.Spider):
    name = 'scrap'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').get()
            author = quote.xpath('.//*[@itemprop="author"]/text()').get()
            tag = quote.xpath('.//*[@class="tag"]/text()').getall()

            yield{
                'text': text,
                'author': author,
                'tag': tag
            }
        next_page = response.xpath('//*[@class="next"]/a/@href').get()
        absolute_next_page = response.urljoin(next_page)
        yield scrapy.Request(absolute_next_page)