from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from src.services.sales.dependencies.dependencies import Dependencies
from src.bootstrap import Bootstrap
from src.settings import Allowed_Origins, Allowed_Methods, Allowed_Headers, Allow_Credentials


@asynccontextmanager
async def lifespan(fast_api_app: FastAPI):
    Bootstrap()
    Dependencies()
    from src.setup import Setup
    await Setup(app=fast_api_app).setup()

    yield

    Setup.shutdown_timer()

app = FastAPI(lifespan=lifespan, docs_url="/swagger")
app.add_middleware(CORSMiddleware,
                   allow_origins=Allowed_Origins,
                   allow_credentials=Allow_Credentials,
                   allow_methods=Allowed_Methods,
                   allow_headers=Allowed_Headers)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"msg": "Bad Request", "detail": exc.errors(), "body": exc.body}),
    )


app.add_exception_handler(exc_class_or_status_code=RequestValidationError, handler=validation_exception_handler)
