from pydantic import BaseModel

from src.schema.user import GetUser
from src.services.service_management.schemas.responses.service import GetService


class GetUserService(BaseModel):
    service: GetService
    price: str
    duration: str

class GetServiceUsers(BaseModel):
    users: list[GetUser]

class GetUserServices(BaseModel):
    services: list[GetUserService]


class ServicesAssignSuccessfully(BaseModel):
    msg: str = f"all services assign to user successfully"