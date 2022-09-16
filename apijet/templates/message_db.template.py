from pydantic import BaseModel


class MessageDB(BaseModel):
    id: str
