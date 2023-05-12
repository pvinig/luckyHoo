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


def generate_token(user_email: str):
    header = {"alg": "RS256"}
    payload = {"email": user_email, "exp": int(time.time() + token_timeout)}
    token = jwt.encode(header, payload, secret)
    return token.decode("utf-8")


def Encode(key: str):
    token = secret.encrypt(key.encode("utf-8"))
    return token.decode("utf-8")


def Decode(key: str):
    token = secret.decrypt(key)
    return token.decode('utf-8')
