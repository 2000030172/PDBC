from pymongo import MongoClient
#creating a pymongo client
client=MongoClient('localhost',27017)
#getting the data connection
db=client['pfsd']
#creating a collection
collection=db['example']
#inserting value into the collection
value1={"name":"Prashanth",
        "age":"20",
        "city":"Nellore"}
collection.insert_one(value1)
print(collection.find_one())
print(collection.fetchall)