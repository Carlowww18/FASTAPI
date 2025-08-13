from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/list")
async def order():
    return {"mensagem":"Você acessou a rota de pedidos"}