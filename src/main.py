import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse
from src.Application.AppSetting import AppSetting
from src.Services.CopyService.dependencies.dependecies import Dependencies as CopyServiceDependencies
from src.bootstrap import Bootstrap



@asynccontextmanager
async def lifespan(app: FastAPI):
    AppSetting()
    Bootstrap()
    CopyServiceDependencies()
    from app.setup import Setup
    await Setup(app=app).setup()

    yield

    Setup.shutdown_timer()

app = FastAPI(lifespan=lifespan, docs_url="/swagger")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"msg": "Bad Request", "detail": exc.errors(), "body": exc.body}),
    )


app.add_exception_handler(exc_class_or_status_code=RequestValidationError, handler=validation_exception_handler)