from pydantic import BaseModel


class ServiceAddedSuccessfully(BaseModel):
    publicId: str
    msg: str = "service added successfully"

class GetService(BaseModel):
    id: int
    title: str
    description: str
    isActive: bool

class GetServices(BaseModel):
    services: list[GetService]