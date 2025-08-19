from pydantic import BaseModel, Field


class PersonType(BaseModel):
    id : int 
    first_name : str
    last_name : str