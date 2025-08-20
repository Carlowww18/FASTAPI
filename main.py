from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from routers.auth_routes import auth_router
from routers.order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

#PARA RODAR O CODIGO NO TERMINAL: uvicorn main:app --reload