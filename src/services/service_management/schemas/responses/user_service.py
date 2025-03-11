from pydantic import BaseModel

from src.services.service_management.schemas.responses.service import GetService


class GetUserService(BaseModel):
    service: GetService
    price: str
    duration: str
