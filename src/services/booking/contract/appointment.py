from typing import NamedTuple

from src.shared.contract.appointment.address import Address
from src.services.booking.contract.user import User
from src.shared.contract.appointment.reservation import Reservation


class AppointmentDto(NamedTuple):
    selected_services: list[int]
    description: str
    client: User
    address: Address
    reservation: Reservation