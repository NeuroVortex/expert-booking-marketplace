from pydantic import BaseModel
from .time import TimeSlotDto


class ReservationDto(BaseModel):
    time_slot: TimeSlotDto
    user_public_id: str
    public_address_id: str
    selectedServices: list[int]
    description: str
