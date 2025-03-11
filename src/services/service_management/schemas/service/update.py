from pydantic import BaseModel


class UpdateService(BaseModel):
    name: str
    description: str
    parent