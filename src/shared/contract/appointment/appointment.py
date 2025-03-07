from typing import NamedTuple

from src.services.booking.contract.client import Client
from src.shared.contract.appointment.reservation import Reservation


class Appointment(NamedTuple):
    id: int
    selected_services: list[int]
    description: str
    client: Client
    reservation: Reservation