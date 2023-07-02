from pymongo import MongoClient


conn = MongoClient('mongodb://admin:admin@localhost:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true')