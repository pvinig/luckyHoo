from src.Data.db import connection
from src.Models.user import *
from src.schemas.jwt import Decode


def get_user():
    return


def check_pwd():
    return

async def check_login(user: Userlogin):
    who = connection.local.user.find_one(user.email)
    key = who
    if who and key == user.pwd:
        return True
    raise Exception('email ou senha nao conferem')