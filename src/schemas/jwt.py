from authlib.jose import jwt
from bson import objectid
import time

token_timeout = 7 * 24 * 3600


def generate_token(user_id: str):
    private_key = "asdd3edadsd23frfedws"
    header = {"alg": "RS256"}
    payload = {"user_id": user_id, "exp": int(time.time() + token_timeout)}
    token = jwt.encode(header, payload, private_key)
    return token
