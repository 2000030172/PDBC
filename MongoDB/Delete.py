from pymongo import MongoClient
#creating a pymongo client
client=MongoClient('localhost',27017)
#getting the data connection
db=client['pfsd']
#creating a collection
collection=db['example']
#inserting value into the collection
data=[{"_id":"1530211012",
       "name":"Prashanth",
        "age":"20",
        "city":"Nellore"},
      {
        "_id":"123456789",
        "name":"Keshanand",
        "age":"21",
        "city":"Produtur"},
      {
        "_id":"534461789",
        "name":"Sushmitha",
        "age":"14",
        "city":"Nellore"
      }]
collection.insert_many(data)
print(collection.inserted_ids)
#Deleting one document
collection.delete_one({"_id":"30172"})
#Retrieving all the records using the find() method
print("Documents in the collection after update operation : ")
for value in collection.find():
    print(value)