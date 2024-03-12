import scrapy


class FourbrickSpider(scrapy.Spider):
    name = "fourbrick"
    allowed_domains = ["froubrick.com"]
    start_urls = ["https://froubrick.com"]

    def start_requests(self):
        urls = [
            "https://www.fourbrick.com/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.css(".wixui-rich-text__text::text").get()
        print("safasfd",data)
        
