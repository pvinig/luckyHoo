from authlib.jose import jwt
from bson import objectid
from cryptography.fernet import Fernet
import time
import re


def clean(txt):
    pwd = re.sub("[^A-Z]+", "", txt, 0, re.I).encode
    return pwd


key = open(".secret.txt").read()
secret = Fernet(key)
token_timeout = 7 * 24 * 3600


def generate_token(user_id: str):
    private_key = "asdd3edadsd23frfedws"
    header = {"alg": "RS256"}
    key = Fernet.generate_key()
    f = Fernet(key)

    payload = {"user_id": user_id, "exp": int(time.time() + token_timeout)}
    token = jwt.encode(header, payload, f)
    return token.decode("utf-8")


def Encode(key: str):
    token = secret.encrypt(key.encode("utf-8"))
    return token.decode("utf-8")


def Decode(key: str):
    token = secret.decrypt(key.encode())
    return token.decode()
