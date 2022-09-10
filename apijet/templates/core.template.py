from {project_name}.models.{endpoint_name} import {endpoint_name}Base, {endpoint_name}Full
from {project_name}.database.{endpoint_name} import get_{endpoint_name}, get_{endpoint_name}_by_id, save_{endpoint_name}

class MatchCore:
    @staticmethod
    def get_all() -> List[{endpoint_name}Full]:
        return list(get_{endpoint_name}())

    @staticmethod
    def save_one(data:{endpoint_name}Base):
        return save_{endpoint_name}(data.dict())
    
    @staticmethod
    def get_one(pid:str) -> {endpoint_name}Full:
       return get_{endpoint_name}_by_id(pid)
