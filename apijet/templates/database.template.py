from {project_name}.database.dbmanager import db

def create_{collection}(data: dict):
    return db['{collection}'].insert_one(data)
   

def read_{collection}_by_id(_id: str):
    return db['{collection}'].find_one({{'_id':'_id'}})
