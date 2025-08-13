from fastapi import FastAPI

app = FastAPI()

from routers.auth_routes import auth_router
from routers.order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

#PARA RODAR O CODIGO NO TERMINAL: uvicorn main:app --reload