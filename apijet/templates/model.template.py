from pydantic import BaseModel, Field
from {project_name}.database.pyobject import PyObjectId


class {endpoint_name}In(BaseModel):
    text:str = 'hello {endpoint_name}'


class {endpoint_name}Out({endpoint_name}In):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
