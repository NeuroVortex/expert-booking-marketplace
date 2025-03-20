from pydantic import BaseModel


class ServiceAddedSuccessfully(BaseModel):
    publicId: str
    msg: str = "service added successfully"

class GetService(BaseModel):
    public_id: str
    title: str
    description: str
    is_active: bool
    photo_path: str | None = None

class GetServices(BaseModel):
    services: list[GetService]

class GetUserService(BaseModel):
    public_id: str
    name: str
    price: str
    duration: str

class GetUserServices(BaseModel):
    users: list[GetUserService]