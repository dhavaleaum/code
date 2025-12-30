
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company"]
emp = db["employee"]

emp.insert_many([
    {"ID":123,"name":"Ravi","dept":"Accounts","phone":111},
    {"ID":210345,"name":"Asha","dept":"HR","phone":222},
])

print("Accounts Dept:")
for e in emp.find({"dept":"Accounts"}):
    print(e)

emp.delete_one({"ID":210345})
emp.update_one({"ID":123},{"$set":{"phone":999}})
