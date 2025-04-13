from pydantic import BaseModel
from datetime import date, time

class TimeSlotDto(BaseModel):
    user_public_id: str
    date: date
    start_time: time
    end_time: time
