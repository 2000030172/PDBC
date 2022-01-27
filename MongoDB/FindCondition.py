from pymongo import MongoClient
#creating a pymongo client
client=MongoClient('localhost',27017)
#getting the data connection
db=client['pfsd']
#creating a collection
collection=db['example']
#inserting value into the collection
data=[{"_id":"1530211",
       "name":"Prashanth",
        "age":"20",
        "city":"Nellore"},
      {
        "_id":"123456",
        "name":"Keshanand",
        "age":"21",
        "city":"Produtur"},
      {
        "_id":"534617",
        "name":"Sushmitha",
        "age":"14",
        "city":"Nellore"
      }]
collection.insert_many(data)
print(collection.inserted_ids)
print(collection.find_one())
#Retrieving the first record using the find() method()
#Data Change
print("Records of the Collection : ")
for val in collection.find():
    print(val)
#Retriving records with age greater than age greater than 18 using the find() method
print("Record whose age is more than 18 : ")
for val in collection.find({"age":{"$gt":"18"}}):
    print(val)