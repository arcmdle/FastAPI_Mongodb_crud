from pymongo import MongoClient

MONGODB_URI = 'mongodb://admin:admin@localhost:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true'

# This can be an environment variable.
conn = MongoClient(MONGODB_URI)