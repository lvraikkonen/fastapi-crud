from fastapi import APIRouter

from models.user import User
from schemas.user import serializeDict, serializeList #userEntity, usersEntity
from bson import ObjectId
from config.db import conn

user = APIRouter()

@user.get('/')
async def find_all_users():
    return serializeList(conn.fastapi.user.find())


@user.get('/{id}')
async def find_one_user(id):
    return serializeDict(conn.fastapi.user.find_one({"_id": ObjectId(id)}))


@user.post('/')
async def create_user(user: User):
    conn.fastapi.user.insert_one(dict(user))
    return serializeList(conn.fastapi.user.find())


@user.put('/{id}')
async def update_user(id, user: User):
    conn.fastapi.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return serializeDict(conn.fastapi.user.find_one({"_id": ObjectId(id)}))


@user.delete('/{id}')
async def delete_user(id):
    return serializeDict(conn.fastapi.user.find_one_and_delete({"_id": ObjectId(id)}))