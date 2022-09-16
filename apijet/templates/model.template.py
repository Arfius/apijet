from pydantic import BaseModel


class {endpoint_name}Base(BaseModel):
    text: str = 'hello {endpoint_name}'
