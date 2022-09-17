from pydantic import BaseModel, Field
from {project_name}.repository.pyobjectid import PyObjectId
from bson import ObjectId


class {endpoint_name}BaseDB(BaseModel):
    text: str = 'hello {endpoint_name}'

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {{ObjectId: str}}
        schema_extra = {{
            "example": {{
                "text": "text"
            }}
        }}


class {endpoint_name}FullDB({endpoint_name}BaseDB):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
