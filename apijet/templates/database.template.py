from repository.dbmanager import db
from bson import ObjectId


def save_{collection}(data: dict):
    return db['{collection}'].insert_one(data)


def get_{collection}_by_id(_id: str):
    return db['{collection}'].find_one({{'_id': ObjectId(_id)}})


def get_{collection}():
    return db['{collection}'].find({{}})
