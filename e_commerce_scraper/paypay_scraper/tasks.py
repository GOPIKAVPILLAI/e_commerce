from celery import shared_task
from scrapy.crawler import CrawlerProcess
from .spiders.rakuma import RakumaSpider
from pydispatch import dispatcher
from .models import product
from scrapy import signals
@shared_task
def run_spider():
    
    process = CrawlerProcess()
    dispatcher.connect(_save_item_to_db,signal=signals.item_scraped)
    process.crawl(RakumaSpider)
    
    process.start()
    
def _save_item_to_db(item,response,spider):
    print("this is item",item)
    product.objects.create(title=item.get('title',''),description=item.get('description',''),status=item.get('status',''),condition=item.get('condition',''))