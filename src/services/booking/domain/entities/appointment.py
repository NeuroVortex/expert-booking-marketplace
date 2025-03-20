from dataclasses import dataclass

from src.services.account_management.domain.user import UserEntity
from src.services.booking.domain.value_objects.address import Address
from src.services.booking.domain.value_objects.reservation import Reservation


@dataclass
class AppointmentEntity:
    public_id: str
    selected_services: list[int]
    description: str
    client: UserEntity
    address: Address
    reservation: Reservation