from pydantic import BaseModel

class Userlogin(BaseModel):
    email: str
    pwd: str
    
    
class User(BaseModel):
    _id: str
    name: str
    email: str
    pwd: str
    
    