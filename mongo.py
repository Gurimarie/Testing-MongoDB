import os
import pymongo
if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

"""" Insert many new lines to database (kept to remember)
new_docs = [{
     "first": "terry",
     "last": "pratchett",
     "dob": "28/04/1948",
     "gender": "m",
     "hair_colour": "not much",
     "occupation": "writer",
     "nationality": "british"
}, {
     "first": "george",
     "last": "rr martin",
     "dob": "20/09/1948",
     "gender": "m",
     "hair_colour": "white",
     "occupation": "writer",
     "nationality": "american"
}]
coll.insert_many(new_docs)

...end of insert many """

coll.update_many({"nationality": "british"}, {"$set": {"hair_colour": "pink"}})

documents = coll.find({"nationality": "british"})

for doc in documents:
    print(doc)
