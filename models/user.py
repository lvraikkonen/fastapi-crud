from enum import Enum
from typing import Optional, List
from pydantic import BaseModel

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