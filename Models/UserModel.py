from pydantic import BaseModel, validator
from Data.db import connection


class User(BaseModel):
    _id: str
    email: str
    pwd: str


class Userlogin(BaseModel):
    email: str
    pwd: str


class userRegister(BaseModel):
    email: str
    pwd: str
    comfirm_pwd: str

    @validator("comfirm_pwd")
    def password_match(cls, validation, values):
        if "pwd" in values and validation != values["pwd"]:
            raise ValueError("as senhas nao conferem")
        return validation
