from pymongo import MongoClient
from {project_name}.project import info
if info['mongo']['auth']:
    db = MongoClient(f"mongodb://{{info['mongo']['username']}}:{{info['mongo']['password']}}@{{info['mongo']['address']}}:{{info['mongo']['port']}}")[f"{{info['name']}}"]
else:
    db = MongoClient(f"mongodb://{{info['mongo']['address']}}:{{info['mongo']['port']}}")[f"{{info['name']}}"]
