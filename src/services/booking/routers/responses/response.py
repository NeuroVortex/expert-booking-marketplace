from pydantic import BaseModel


class Appointment(BaseModel):
    time: str
    available: bool

class Schedules(BaseModel):
    schedules: list[Appointment]