# fastapi-crud
Basic CRUD operations using FastAPI and MongoDB

## Prerequisites

1. FastAPI basics
2. Python installed 
3. Mongodb Community server installed


## Install Dependencies

1. fastAPI
2. uvicorn
3. pymongo

```shell
$ pip install fastapi uvicorn pymongo pymongo[srv]
```

## Create the Project structure


## Edit index.py

```python
from fastapi import FastAPI

app = FastAPI()
```

run the server

## Edit database.py

create a file called config/db.py and add the following content inside of it

```python
from pymongo import MongoClient

conn = MongoClient("mongodb+srv://biuser:<password>@claus-mongo-cluster.2skj4.azure.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = conn.fastapi

collection_name = db["user"]
```


## Create the models, schemas

model User

``` python
from typing import Optional, List
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str
    gender: Gender
    role: List[Role]
    comment: Optional[str]
```

schema to serialize

``` python
def serializeDict(item) -> dict:
    new_dict = {**{i: str(item[i]) for i in item if i=="_id"}, **{i: item[i] for i in item if i!="_id"}}
    return new_dict

def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]
```

## Build The CRUD API in routes module

``` python
from fastapi import APIRouter

from models.user import User


user = APIRouter()

@user.get('/')
async def find_all_users():
    pass


@user.get('/{id}')
async def find_one_user(id):
    pass


@user.post('/')
async def create_user(user: User):
    pass


@user.put('/{id}')
async def update_user(id, user: User):
    pass


@user.delete('/{id}')
async def delete_user(id):
    pass
```