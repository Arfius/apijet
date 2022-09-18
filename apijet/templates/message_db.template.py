from pydantic import BaseModel
from typing import Optional


class MessageDB(BaseModel):
    id: Optional[str]
    modified_count:Optional[int]
    deleted_count:Optional[int]