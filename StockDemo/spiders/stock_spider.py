import scrapy


class StockInfoSpider(scrapy.Spider):
    name = "stock_info"
    allowed_domains = ["10jqka.com"]
    start_urls = [
        "http://data.10jqka.com.cn/",
        "http://data.10jqka.com.cn/market/zdfph/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
