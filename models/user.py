from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    full_name: str
    email: str
    password:str

