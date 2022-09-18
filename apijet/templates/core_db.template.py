from typing import List
from {project_name}.models.message_db import MessageDB
from {project_name}.models.{endpoint_name} import {endpoint_name}BaseDB, {endpoint_name}FullDB
from {project_name}.repository.{endpoint_name} import get_{endpoint_name}
from {project_name}.repository.{endpoint_name} import save_{endpoint_name}
from {project_name}.repository.{endpoint_name} import update_{endpoint_name}
from {project_name}.repository.{endpoint_name} import get_all_{endpoint_name}
from {project_name}.repository.{endpoint_name} import delete_{endpoint_name}


class {endpoint_name}Core:
    @staticmethod
    def get_all() -> List[{endpoint_name}FullDB]:
        return list(get_all_{endpoint_name}())

    @staticmethod
    def get_one(pid: str) -> {endpoint_name}FullDB:
        return get_{endpoint_name}(pid)

    @staticmethod
    def save_one(data: {endpoint_name}BaseDB) -> MessageDB:
        ret = save_{endpoint_name}(data.dict())
        return MessageDB(id=str(ret.inserted_id))
    
    @staticmethod
    def update_one(pid:str, data: {endpoint_name}FullDB) -> MessageDB:
        ret = update_{endpoint_name}(pid, data.dict())
        return MessageDB(modified_count=str(ret.modified_count))

    @staticmethod
    def delete_one(pid: str) -> MessageDB:
        ret = delete_{endpoint_name}(pid)
        return MessageDB(deleted_count=str(ret.deleted_count))