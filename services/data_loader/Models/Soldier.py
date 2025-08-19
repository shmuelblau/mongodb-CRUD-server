from pydantic import BaseModel, Field 
from typing import Optional 


class Soldier(BaseModel):
    id : int 
    first_name : Optional[str]
    last_name : Optional[str]
    rank: Optional[str]
    phone_number:Optional[int]