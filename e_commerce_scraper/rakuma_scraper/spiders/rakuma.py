
import scrapy
from ..items import ProductItem
class RakumaSpider(scrapy.Spider):
    name = "rakuma"
    start_urls = ['https://fril.jp/category/10001']

    def parse(self, response):
        
        for product in response.css("p[class=item-box__item-name]"):
            with open("myfile.txt", "a") as f:
                title = product.css('a::attr(title)').get()
                desc=product.css('a::attr(onclick)').get()
                f.write(f"title={title}\ndesc={desc}\n\n")
            item=ProductItem()
            
            item['title'] = title,
            item['description']= desc,
            item['status']= "Avalible"
            item['condition']= "New"
            
            yield item

        next_page = response.css('a.Pagination-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
