import scrapy
class ProductItem(scrapy.Item):
    title=scrapy.Field()
    description=scrapy.Field()
    status=scrapy.Field()
    condition=scrapy.Field()