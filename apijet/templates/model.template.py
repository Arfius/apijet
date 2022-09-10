from pydantic import BaseModel, Field
from database.pyobjectid import PyObjectId
from bson import ObjectId

class {endpoint_name}Base(BaseModel):
    text:str = 'hello {endpoint_name}'
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {{ObjectId: str}}
        schema_extra = {{
            "example": {{
                "text": "text"
            }}
        }}


class {endpoint_name}Full({endpoint_name}Base):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
