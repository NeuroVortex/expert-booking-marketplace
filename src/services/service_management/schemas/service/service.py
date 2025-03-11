from pydantic import BaseModel, Field


class Service(BaseModel):
    name: str
    description: str
    parentServiceId: int | None = Field(None, gt=0)
