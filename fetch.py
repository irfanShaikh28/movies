import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mongodb"]
mycol = mydb["mydb"]

x mycol.find_one()

print(x)
