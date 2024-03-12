import scrapy


class CompaniesSpider(scrapy.Spider):
    name = "companies"
    allowed_domains = ["naukri.com"]
    start_urls = ["https://www.naukri.com"]

    def start_requests(self):
        urls = [
            "https://www.naukri.com/companies-in-delhi-ncr-l9508",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.css(".freeTuple ")
        for item in data:
            print("sfsfasfdasdas",item)

