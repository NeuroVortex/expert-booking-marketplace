from fastapi import APIRouter

from src.app.router.response import AppResponse

app_router = APIRouter()


@app_router.get("/")
async def application() -> AppResponse:
    return AppResponse()