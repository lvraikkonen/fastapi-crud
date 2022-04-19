from fastapi import APIRouter, Depends
from auth.auth_bearer import JWTBearer


test_routes = APIRouter()

@test_routes.get('/greeting/{user_name}', dependencies=[Depends(JWTBearer())], tags=["test"])
async def greetings(user_name: str):
    return {"Hello": user_name}