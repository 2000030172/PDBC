from pymongo import MongoClient
#creating a pymongo client
client=MongoClient('localhost',27017)
#getting the data connection
db=client['pfsd']
#creating a collection
collection=db['example']
#inserting value into the collection
data=[{"_id":"2000030172",
       "name":"Prashanth",
        "age":"20",
        "city":"Nellore"},
      {
        "_id":"9920004778",
        "name":"Keshanand",
        "age":"21",
        "city":"Produtur"},
      {
        "_id":"5344617",
        "name":"Sushmitha",
        "age":"14",
        "city":"Nellore"
      }]
collection.insert_many(data)
print(collection.find_one())
print(collection.inserted_ids)