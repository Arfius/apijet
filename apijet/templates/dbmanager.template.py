from pymongo import MongoClient
db = MongoClient("mongodb://127.0.0.1:27017")["{database_name}"]