from pydantic import BaseModel
from datetime import datetime
from .client import Client


class Appointment(BaseModel):
    client: Client
    datetime: datetime
    selectedServices: list[int]
    description: str
