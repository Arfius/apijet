from {project_name}.repository.dbmanager import db
from bson import ObjectId


def get_all_{collection}():
    return db['{collection}'].find({{}})


def save_{collection}(data: dict):
    return db['{collection}'].insert_one(data)


def update_{collection}(pid:str, data: dict):
    value_to_set = {{"$set": data}}
    return db['{collection}'].update_one( {{'_id':ObjectId(pid)}}, value_to_set)


def delete_{collection}(pid: str):
    return db['{collection}'].delete_one({{'_id':ObjectId(pid)}})



def get_{collection}(pid: str):
    return db['{collection}'].find_one({{'_id':ObjectId(pid)}})

