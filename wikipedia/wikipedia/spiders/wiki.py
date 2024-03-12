#https://www.wikipedia.org/
import scrapy
import datetime
from pymongo import MongoClient
client = MongoClient("mongodb+srv://amarnath:scrap3142@cluster0.ipuz3gi.mongodb.net/")
db = client.wikipedia
collection = db.wikipediaOrg

def insertToDb(title, tagline):
    data = {
        "title":title,
        "tagline":tagline,
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }
    inserted_data = collection.insert_one(data).inserted_id
    print("ssafasdfasdfasfdinserted_data",inserted_data)
    


title_list = []
tagline_list = []
class WikiSpider(scrapy.Spider):
    
    name = "wiki"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://www.wikipedia.org"]

    def start_requests(self):
        urls = [
            "https://www.wikipedia.org/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        #collecting the data
        data = response.css(".other-project")
        for item in data:
            title =  item.css(".other-project-title::text").get()
            title_list.append(title)
            tagline = item.css(".other-project-tagline::text").get()
            tagline_list.append(tagline)
            print("tagasdfsafasfda",tagline)
            insertToDb(title,tagline)
            
        
        