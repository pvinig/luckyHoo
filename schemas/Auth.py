from Data.db import connection
from Models.UserModel import *


async def Login(user: Userlogin):
    if await connection.local.user.find_one(dict(user)):
        return [{"email": user.email}]
    return 400
    

async def Register(user: Login):
    if await connection.local.user.find_one({"email": "{user.email}"}): 
        return 400
    elif user.pwd != user.cpwd :
        return Exception("as senhas nao batem")
    
    newUser: User = [{"email":"{user.email}", "pwd":"{user.pwd}"}]
    
    User = await connection.local.user.insert_one(dict(newUser))
        
    
    return newUser