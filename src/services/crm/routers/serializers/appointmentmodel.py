from pydantic import BaseModel
from datetime import datetime
from .client import Client


class AppointmentModel(BaseModel):
    client: Client
    datetime: datetime
    selectedServices: list[int]
    description: str
