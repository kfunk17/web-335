# ============================================
# ; Title:  funk-user-service.py
# ; Author: Professor Krasso
# ; Modified by: Karie Funk
# ; Date:  10 December 2019
# ; Description:  query and create documents 
# ; in MongoDB instance
# ;===========================================

import pymongo
import pprint
import datetime

from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.web335

user = {

    "first_name": "Claude",

    "last_name": "Debussy",

    "email": "cdebussy@me.com",

    "employee_id": "0000008",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

print(client)

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000008"}))

employee_id = "0000008"

pprint.pprint(db.users.find_one({"employee_id": employee_id}))