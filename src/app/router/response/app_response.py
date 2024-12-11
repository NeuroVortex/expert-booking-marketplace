from pydantic import BaseModel


class AppResponse(BaseModel):
    msg: str = 'App is up and running'