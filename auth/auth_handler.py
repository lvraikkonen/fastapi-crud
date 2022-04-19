# This file is responsible for signing, encoding, decoding and returning JWTS
import time
from typing import Dict

import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# function returns the generated Tokens (JWTs)
def token_response(token: str):
    return {
        "access token": token
    }


def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] > time.time() else None
    except:
        return {}