from pymongo import MongoClient

db_name={database_name}
collection = {collection}
db = MongoClient({database_url})[db_name]


def create_{endpoint}(data:dict()):

   

def read__{endpoint}_by_id(_id: str):
    return db[{collection}].find_one({'_id':_id})
