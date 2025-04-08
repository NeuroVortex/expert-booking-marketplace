from datetime import timedelta
from typing import List
from pydantic import BaseModel


class UserServiceDto(BaseModel):
    public_id: str
    price: str
    duration: timedelta

class UserServicesDto(BaseModel):
    public_user_id: str
    services: List[UserServiceDto]

class UnassignUserServices(BaseModel):
    public_user_id: str
    services_public_ids: List[str]

