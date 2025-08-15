from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/auth")
async def auth():
    return {"mensagem": "Você acessou a rota de auth",
            "autenticado": False}

@auth_router