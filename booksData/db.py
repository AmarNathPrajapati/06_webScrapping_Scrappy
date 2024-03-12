import datetime
from pymongo import MongoClient
client = MongoClient("mongodb+srv://amarnath:scrap3142@cluster0.ipuz3gi.mongodb.net/")
db = client.test_database
collection = db.test_collection
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print("sfasfadfsasdf",post_id)
