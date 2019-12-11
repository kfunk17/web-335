# ============================================
# ; Title:  funk-user-service.py
# ; Author: Professor Krasso
# ; Modified by: Karie Funk
# ; Date:  10 December 2019
# ; Description:  updating and deleting 
# ; documents
# ;===========================================


from pymongo import MongoClient

import pprint
import pymongo
import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(

    {"employee_id": "0000008"},

    {

        "$set": {

            "email": "kfunk@my365.bellevue.edu"

        }

    }

)

pprint.pprint(db.users.find_one({"employee_id": "0000008"}, {"email": 1, "employee_id": 1, "first_name": 1, "last_name": 1}))