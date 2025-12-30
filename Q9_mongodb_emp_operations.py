
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company"]
emp = db["EMP"]

emp.insert_many([
    {"name":"Riddhi","mobile":111,"sal":8000,"age":23},
    {"name":"Amit","mobile":222,"sal":6000,"age":25},
])

print("Salary 5000-10000")
for e in emp.find({"sal":{"$gte":5000,"$lte":10000}}):
    print(e)

emp.update_one({"name":"Riddhi"},{"$set":{"mobile":999}})

print("Sorted by age")
for e in emp.find().sort("age",1):
    print(e)
