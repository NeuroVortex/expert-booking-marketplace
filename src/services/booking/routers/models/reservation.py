from pydantic import BaseModel
from datetime import datetime
from .user import UserModel


class ReservationModel(BaseModel):
    userInfo: UserModel
    bookedTime: datetime
    selectedServices: list[int]
    description: str
