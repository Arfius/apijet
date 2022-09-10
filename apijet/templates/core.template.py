from typing import List
from database.message import Message
from models.{endpoint_name} import {endpoint_name}Base, {endpoint_name}Full
from database.{endpoint_name} import get_{endpoint_name}, get_{endpoint_name}_by_id, save_{endpoint_name}

class {endpoint_name}Core:
    @staticmethod
    def get_all() -> List[{endpoint_name}Full]:
        return list(get_{endpoint_name}())

    @staticmethod
    def save_one(data:{endpoint_name}Base) -> Message:
        id = save_{endpoint_name}(data.dict())
        return Message(id=str(id.inserted_id))
    
    @staticmethod
    def get_one(pid:str) -> {endpoint_name}Full:
        return {endpoint_name}Full(**get_{endpoint_name}_by_id(pid))
