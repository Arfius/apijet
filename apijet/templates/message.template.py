from pydantic import BaseModel
from bson import ObjectId

class Message(BaseModel):
    id: ObjectId
