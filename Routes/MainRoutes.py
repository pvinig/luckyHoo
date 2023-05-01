from fastapi import APIRouter
from schemas.Serializers import *
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
     return serializeList(connection.local.user.find())
 
@api.post("/newbie")
async def CreateUser(user: User):


    connection.local.user.insert_one(dict(user))
    usuario = serializeDict(user)  
     
    return usuario