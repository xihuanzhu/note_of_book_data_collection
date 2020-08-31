from scrapy.selector import Selector
from scrapy import Spider
from mySpider.items import Article
class ArticleSpider(Spider):
    name="article"
    allowed_domains = ["https://blog.csdn.net/"]
    start_urls = ["https://blog.csdn.net/serverke/article/details/108140525"]
    #rules = [Rule(SgmlLinkExtractor(allow=('(/wiki/)((?!:).)*$'),),callback="parse_item", follow=True)]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: "+title)
        item['title'] = title
        return item