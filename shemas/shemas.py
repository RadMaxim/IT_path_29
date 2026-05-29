from pydantic import BaseModel

class Data(BaseModel):
    name: str
    age: int
class Android(BaseModel):
    name: str
    age: int
    model:int
    address:str|None
    whereMade:str|int