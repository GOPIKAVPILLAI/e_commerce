# import scrapy


# class YahooAuctionSpider(scrapy.Spider):
#     name = "yahoo_auction"
#     allowed_domains = ["auctions.yahoo.co.jp"]
#     start_urls = ["https://auctions.yahoo.co.jp"]

#     def parse(self, response):
#         pass
import scrapy

class YahooAuctionSpider(scrapy.Spider):
    name = "yahoo_auction"
    start_urls = ['https://auctions.yahoo.co.jp/']

    def parse(self, response):
        for product in response.css('div.Product'):
            yield {
                'title': product.css('h3.ProductTitle::text').get(),
                'description': product.css('p.ProductDescription::text').get(),
                'status': product.css('span.ProductStatus::text').get(),
                'condition': product.css('span.ProductCondition::text').get(),
            }

        next_page = response.css('a.Pagination-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
