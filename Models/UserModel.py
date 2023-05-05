from pydantic import BaseModel, validator


class Userlogin(BaseModel):
    email: str
    pwd: str


class User(BaseModel):
    _id: str
    name: str
    email: str
    pwd: str


class userRegister(BaseModel):
    email: str
    pwd: str
    comfirm_pwd: str

    @validator('comfirm_pwd')
    def pwd_match(cls, validation, values):
        if 'pwd' in values and validation != ['pwd']:
            raise ValueError('as senhas nao conferem')
        return validation
