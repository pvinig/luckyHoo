from fastapi import APIRouter, Form, File
from schemas.Serializers import *
from bson import ObjectId

# from schemas.Auth import *
from Models.UserModel import *
from Data.db import connection
from typing import Annotated

# from bson import ObjectId

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
    new_user = Userlogin(email=user.email, pwd=user.pwd)
    AlreadyIn = connection.local.user.find_one({"email": user.email})
    if AlreadyIn:
        raise ValueError("email ja cadastrado")

    connection.local.user.insert_one(dict(new_user))

    return new_user


@api.post("/login")
async def Login(user: Userlogin):
    if connection.local.user.find_one(dict(user)):
        return [200, {"email": user.email}]
    return Exception("email ou senha incorretos!")


@api.delete("/{id}")
async def delete_user(id):
    return serializeDict(
        connection.local.user.find_one_and_delete({"_id": ObjectId(id)})
    )
