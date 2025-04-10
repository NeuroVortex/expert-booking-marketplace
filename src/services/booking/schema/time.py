from pydantic import BaseModel
from datetime import date, time

class TimeSlotDto(BaseModel):
    date: date
    start_time: time
    end_time: time
    time_period: str