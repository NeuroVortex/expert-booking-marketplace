from pydantic import BaseModel

from src.schema.user import GetUser
from src.services.service_management.schemas.responses.service import GetService


class GetUserService(BaseModel):
    public_id: str
    user: GetUser
    service: GetService
    price: str
    duration: str

class GetServiceUsers(BaseModel):
    users: list[GetUser]

class GetUserServices(BaseModel):
    user_services: list[GetUserService]


class ServicesAssignSuccessfully(BaseModel):
    msg: str = f"all services assign to user successfully"

class ServicesUnassignSuccessfully(BaseModel):
    msg: str = f"all services unassign successfully"