# import scrapy


# class PaypaySpider(scrapy.Spider):
#     name = "paypay"
#     allowed_domains = ["paypayfleamarket.yahoo.co.jp"]
#     start_urls = ["https://paypayfleamarket.yahoo.co.jp"]

#     def parse(self, response):
#         pass
import scrapy
from ..models import product
from ..items import ProductItem
class PaypaySpider(scrapy.Spider):
    
    def __init__(self):
        print("$$$$$$$$$$$$$$$$$$$$$$\n\n\n\n\n I GOT INITIALIZED\n\n\n\n\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    name = "paypay"
    start_urls = ['https://paypayfleamarket.yahoo.co.jp/']
    # allowed_domains = ["paypayfleamarket.yahoo.co.jp"]
     
    def parse(self, response):
        productset=[]
        print("#################\n\n\n\n\n\n HELLLLLLOOOOOOOOOOOO \n\n\\n")
        print(response.text)
        for product in response.css("img"):
            with open("myfile.txt", "a") as f:
                f.write(str(product))
            item=ProductItem()
            
            item['title'] = product.css('h3.ProductTitle::text').get(),
            item['description']= product.css('p.ProductDescription::text').get(),
            item['status']= product.css('span.ProductStatus::text').get(),
            item['condition']= product.css('span.ProductCondition::text').get(),
            yield item
        # next_page = response.css('a.Pagination-next::attr(href)').get()
        # if next_page:
        #     yield response.follow(next_page, self.parse)
       