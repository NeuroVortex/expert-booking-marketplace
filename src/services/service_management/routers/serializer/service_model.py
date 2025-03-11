from pydantic import BaseModel


class ServiceModel(BaseModel):
    name: str
    description: str
    parentServiceId: int | None

