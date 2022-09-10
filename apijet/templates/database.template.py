from {project_name}.database.dbmanager import db

def save_{collection}(data: dict):
    return db['{collection}'].insert_one(data)
   

def get_{collection}_by_id(_id: str):
    return db['{collection}'].find_one({{'_id':'_id'}})


def get_{collection}():
    return db['{collection}'].find({{}}))