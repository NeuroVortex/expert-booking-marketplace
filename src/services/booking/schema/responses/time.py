from pydantic import BaseModel
from datetime import date, time

from src.schema.user import GetUser


class GetTimeSlot(BaseModel):
    service_provider: GetUser
    time_slot_public_id: str
    date: date
    start_time: time
    end_time: time
    is_booked: bool


class GetTimeSlots(BaseModel):
    time_slots: list[GetTimeSlot]
