from fastapi import FastAPI
from routes.user import user
from routes.other_routes import test_routes
from routes.login import login

app = FastAPI()

app.include_router(user)
app.include_router(test_routes)
app.include_router(login)