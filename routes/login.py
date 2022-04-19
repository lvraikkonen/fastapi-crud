from fastapi import APIRouter, Body
from config.db import conn

from models.user import UserSchema, UserLoginSchema
from auth.auth_handler import signJWT

login = APIRouter()

# default user for login
users = [
    # UserSchema("claus", "claus.lv@test.com", "123")
]

def check_user(data: UserLoginSchema):
    user = conn.fastapi.userlogin.find_one({"email": data.email})
    if user:
        return True
    return False
    # for user in users:
    #     if user.email == data.email and user.password == data.password:
    #         return True
    # return False

@login.post('/user/signup', tags=["user"])
async def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    conn.fastapi.userlogin.insert_one(dict(user))
    return signJWT(user.email)


@login.post('/user/login', tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

