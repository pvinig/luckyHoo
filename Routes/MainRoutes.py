from fastapi import APIRouter
from schemas.Serializers import *
# from schemas.Auth import *
from Models.UserModel import *
from Data.db import connection
# from bson import ObjectId

api = APIRouter()


@api.get('/')
async def ola():
    ola = "ola"
    return ola


@api.get("/allUsers")
async def GetUsers():
    x = serializeList(connection.local.user.find())

    return x


@api.post("/Register")
async def Register(user: Userlogin, cpwd: str):
    if connection.local.user.find_one({user.email}):
        return Exception("Email ja cadastrado")
    elif user.pwd != cpwd:
        return Exception("as senhas nao batem")

    connection.local.user.insert_one(dict(user))

    return user


@api.post("/login")
async def Login(user: Userlogin):
    if connection.local.user.find_one(dict(user)):
        return [200, {"email": user.email}]
    return Exception("email ou senha incorretos!")
