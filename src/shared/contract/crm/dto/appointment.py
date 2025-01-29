from typing import NamedTuple

from src.services.crm.contract.address import Address
from src.services.crm.contract.user import User
from src.services.crm.contract.reservation import Reservation


class AppointmentDto(NamedTuple):
    selected_services: list[int]
    description: str
    client: User
    address: Address
    reservation: Reservation