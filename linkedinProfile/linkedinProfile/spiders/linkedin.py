import scrapy


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["linkedin.com"]
    start_urls = ["https://www.linkedin.com"]

    def start_requests(self):
        urls = [
            "https://www.linkedin.com/in/reidhoffman",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        item = response.css(".text-heading-xlarge::text").get()
        print("ssadfasfasfda",item)
