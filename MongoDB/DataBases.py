from pymongo import MongoClient
#creating a pymongo client
client=MongoClient('localhost',27017)
#getting the data connection
db=client['pfsd']
print("Data base created.....!")
#Verification
print("List of Databases after creating new one")
print(client.list_database_names())