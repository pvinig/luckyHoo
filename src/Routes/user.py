from fastapi import APIRouter, Form, File
from src.schemas.Serializers import *
from src.schemas.jwt import *
from bson import ObjectId, objectid

# from schemas.Auth import *
from src.Models.user import *
from src.Data.db import connection
from typing import Annotated

# from bson import ObjectId

api = APIRouter()


@api.get("/")
async def ola():
    connection.local.user.__new__
    ola = "ola"
    return ola


@api.get("/allUsers")
async def GetUsers():
    return serializeList(connection.local.user.find())


@api.post("/Register")
async def Register(user: userRegister):
    new_user = Userlogin(email=user.email, pwd=user.pwd)
    AlreadyIn = connection.local.user.find_one({"email": user.email})
    if AlreadyIn:
        raise ValueError("email ja cadastrado")

    connection.local.user.insert_one(dict(new_user))

    return new_user


@api.post("/login")
async def Login(user: Userlogin):
    login = connection.local.user.find_one(dict(user))

    if login:
        return generate_token(login["email"])
    return Exception("email ou senha incorretos!")


@api.delete("/{id}")
async def delete_user(id):
    return serializeDict(
        connection.local.user.find_one_and_delete({"_id": ObjectId(id)})
    )
