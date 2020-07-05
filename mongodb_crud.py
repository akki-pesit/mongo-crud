import pymongo


def check_if_database_exists(dbname):
    print(myclient.list_database_names())
    dblist = myclient.list_database_names()
    if dbname in dblist:
        print("The database exists")


def check_if_collection_exists(collection_name):
    print(mydb.list_collection_names())
    collist = mydb.list_collection_names()
    if collection_name in collist:
        print("Collection exists")


def create_connection():
    port = "27017"
    host = "localhost"
    return pymongo.MongoClient("mongodb://", host, ":", port, "/")


def insert_documents(documents, mycoll):
    x_insert = mycoll.insert_many(documents)
    return x_insert


def insert_document(document, mycoll):
    x_insert = mycoll.insert_one(document)
    return x_insert


myclient = create_connection()

mydb = myclient["mydatabase"]

mycoll = mydb["customers"]

mydict = {"name": "Sherlock Holmes", "address": "221b Baker Street, London"}

x_insert_one = mycoll.insert_one(mydict)
print("Inserted one doc: ", x_insert_one.inserted_id)

mylist = [
  {"name": "Amy", "address": "Apple st 652"},
  {"name": "Hannah", "address": "Mountain 21"},
  {"name": "Michael", "address": "Valley 345"},
  {"name": "Sandy", "address": "Ocean blvd 2"},
  {"name": "Betty", "address": "Green Grass 1"},
  {"name": "Richard", "address": "Sky st 331"},
  {"name": "Susan", "address": "One way 98"},
  {"name": "Vicky", "address": "Yellow Garden 2"},
  {"name": "Ben", "address": "Park Lane 38"},
  {"name": "William", "address": "Central st 954"},
  {"name": "Chuck", "address": "Main Road 989"},
  {"name": "Viola", "address": "Sideway 1633"}
]

x_insert_many = mycoll.insert_many(mylist)
print("Inserted many docs: ", x_insert_many.inserted_ids)

print("All our agents: ")
for doc in mycoll.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(doc)

print("Your case will be solved by: ", mycoll.find_one())

print("Searching for names starting with S")
myquery = {"name": {"$regex": "^S"}}
mydoc = mycoll.find(myquery).sort("name")

for doc in mydoc:
    print(doc)

check_if_database_exists("mydatabase")
check_if_collection_exists("customers")

mycoll.drop()