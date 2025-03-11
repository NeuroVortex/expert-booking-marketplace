from pydantic import BaseModel


class ServiceAddedSuccessfully(BaseModel):
    publicId: str

class GetService(BaseModel):
    id: int
    title: str
    description: str
    duration: str
    price: str
    selected: bool

class GetServices(BaseModel):
    services: list[GetService]