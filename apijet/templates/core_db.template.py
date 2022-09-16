from typing import List
from models.message_db import MessageDB
from models.{endpoint_name} import {endpoint_name}BaseDB, {endpoint_name}FullDB
from repository.{endpoint_name} import get_{endpoint_name}, get_{endpoint_name}_by_id, save_{endpoint_name}


class {endpoint_name}Core:
    @staticmethod
    def get_all() -> List[{endpoint_name}FullDB]:
        return list(get_{endpoint_name}())

    @staticmethod
    def save_one(data: {endpoint_name}BaseDB) -> MessageDB:
        id = save_{endpoint_name}(data.dict())
        return MessageDB(id=str(id.inserted_id))
    
    @staticmethod
    def get_one(pid: str) -> {endpoint_name}FullDB:
        return {endpoint_name}FullDB(**get_{endpoint_name}_by_id(pid))
