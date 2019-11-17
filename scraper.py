from scrapers.cfb.teams import scrape, compile_rankings

# final = scrape(1, 12, 2019)
# compile_rankings(final)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# databaseName = "cfb-scraper"
databaseName = "test"

dblist = client.list_database_names()
if databaseName in dblist:
    print("The " + databaseName + " exists.")
else:
    print("The " + databaseName + " does not exists.")

database = client[databaseName]

# teamsTable = "teams"
teamsTable = "test"

collist = database.list_collection_names()
if teamsTable in collist:
    print("The " + teamsTable + " collection exists.")
else:
    print("The " + teamsTable + " collection does not exists.")

teams = database[teamsTable]

mydict = { "name": "Test" }

x = teams.insert_one(mydict)

print(x)

mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
]

x = teams.insert_many(mylist)

print(x)

x = teams.find_one()

print(x)

x = teams.find()

print(x)

for x in teams.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(x)

myquery = { "address": "Park Lane 38" }

mydoc = teams.find(myquery)

for x in mydoc:
    print(x)

myquery = { "address": { "$gt": "S" } }

mydoc = teams.find(myquery).sort("name", -1).limit(5)

for x in mydoc:
    print(x)

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

teams.update_one(myquery, newvalues)

for x in teams.find():
    print(x)

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = teams.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

x = teams.estimated_document_count()

print(x)

x = teams.delete_many({})

print(x.deleted_count)

x = teams.estimated_document_count()

print(x)
