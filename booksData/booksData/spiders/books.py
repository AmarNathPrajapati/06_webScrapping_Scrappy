#https://books.toscrape.com/
import scrapy
from pathlib import Path

#storing the data into the database
import datetime
from pymongo import MongoClient
client = MongoClient("")# Add mongodb URI
db = client.booksToScrap

#function to store the data that we scrap from the website
def insertToDb(page, title, image, price,  rating, availability):
    collection = db[page]
    post = {
    "title":title,
    "image":image,
    "price":price,
    "rating":rating,
    "availability":availability,
     "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }   
    post_id = collection.insert_one(post).inserted_id
    print("sfasfadfsasdf",post_id)
    
    
    
class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com"]
    
    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        #scrapping the cards
        cards = response.css(".product_pod")
        print("sfsfsd",cards)
        for card in cards:
            title =  card.css("h3>a::text").get()
            # print("asfsfsasdfsa",title)
            image = card.css(".image_container img")
            image_data = image.attrib["src"].replace("../../../../","https://books.toscrape.com/")
            print("imgagasfasfasf",image.attrib["src"])
            price = card.css(".price_color::text").get()
            # print("pricesfsdfad",price)
            rating = card.css(".star-rating").attrib["class"].split(" ")[1]
            # print("ratingasdfasdf",rating)
            availability = card.css(".availability")
            if(len(availability.css(".icon-ok"))>0):
                inStock = True
            else:
                inStock = False
            # print("avaiasfsffs",availability)
            insertToDb(page,title,image_data, price, rating, inStock)

