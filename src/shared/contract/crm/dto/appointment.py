from typing import NamedTuple

from src.services.booking.contract.address import Address
from src.services.booking.contract.user import User
from src.services.booking.contract.reservation import Reservation


class AppointmentDto(NamedTuple):
    selected_services: list[int]
    description: str
    client: User
    address: Address
    reservation: Reservation