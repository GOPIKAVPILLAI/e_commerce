# import scrapy


# class DigimartSpider(scrapy.Spider):
#     name = "digimart"
#     allowed_domains = ["digimart.net"]
#     start_urls = ["https://digimart.net"]

#     def parse(self, response):
#         pass
import scrapy

class DigiMartSpider(scrapy.Spider):
    name = "digimart"
    start_urls = ['https://www.digimart.net/']

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
