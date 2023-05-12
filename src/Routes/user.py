from fastapi import APIRouter, Form, File
from src.schemas.jwt import *
from src.schemas.Serializers import *
from src.schemas.user import *
from bson import ObjectId, objectid

from src.Models.user import *
from src.Data.db import connection
from typing import Annotated


api = APIRouter()


@api.get("/")
async def ola():
    ola = "ola"
    return ola


@api.get("/allUsers")
async def GetUsers():
    return serializeList(connection.local.user.find())


@api.post("/Register")
async def Register(user: userRegister):
    AlreadyIn = connection.local.user.find_one({"email": user.email})
    if AlreadyIn:
        raise ValueError("email ja cadastrado")

    pwd = Encode(user.pwd)
    new_user = Userlogin(email=user.email, pwd=pwd)

    connection.local.user.insert_one(dict(new_user))

    return new_user


@api.post("/login")
async def Login(user: Userlogin):
    
    if await check_login(user):
        token = generate_token(user.email.__str__())
        if token:
            return token
    raise Exception("email ou senha incorretos!")


@api.delete("/{id}")
async def delete_user(id):
    return serializeDict(
        connection.local.user.find_one_and_delete({"_id": ObjectId(id)})
    )
