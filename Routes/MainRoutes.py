from fastapi import APIRouter, Form, File
from schemas.Serializers import *

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
async def Register(user: userRegister = Form(...)):
    new_user = {"email": f"{user.email}", "pwd": f"{user.pwd}"}

    AlreadyIn = connection.local.user.find(new_user[0])
    if AlreadyIn:
        raise ValueError("email ja cadastrado")

    connection.local.user.insert_one(new_user)

    return new_user


@api.post("/login")
async def Login(user: Userlogin):
    if connection.local.user.find_one(dict(user)):
        return [200, {"email": user.email}]
    return Exception("email ou senha incorretos!")
