import time
from typing import Dict
import jwt

JWT_SECRET = "dsafsdffgfcxzc-*s**saf"
JWT_ALGORITHM = "HS256"


def token_response(token: str):
    return {
        "access_token": token
    }  

def signJWT(UserId: str) -> Dict[str, str]:
    payload = {
        "UserId": UserId,
        "expires": time.time() + 9000000000
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}