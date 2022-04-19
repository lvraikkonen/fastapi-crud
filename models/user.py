from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    name: str
    email: str
    password: str
    gender: Gender
    role: List[Role]
    comment: Optional[str]

class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo" : {
                "name": "Claus",
                "email": "test@test.com",
                "password": "123"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo" : {
                "email": "test@test.com",
                "password": "123"
            }
        }