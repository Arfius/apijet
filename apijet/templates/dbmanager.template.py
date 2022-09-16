from pymongo import MongoClient
from project import info
db = MongoClient(f"mongodb://{info['mongo_address']}:{info['mongo_port']}")[f"{info['name']}"]
