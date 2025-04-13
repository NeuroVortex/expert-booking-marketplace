from pydantic import BaseModel

from src.schema.user import GetUser
from src.services.account_management.schemas.responses.address import GetAddress
from src.services.booking.schema.responses.time import GetTimeSlot
from src.services.service_management.schemas.responses.service import GetService


class GetReservation(BaseModel):
    reserved_phone: str


class GetAppointment(BaseModel):
    public_id: str
    selected_services: list[GetService]
    time_slot: GetTimeSlot
    description: str
    address: GetAddress
    reservation: GetReservation

class GetAppointments(BaseModel):
    client: GetUser
    appointments: list[GetAppointment]