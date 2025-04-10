from dataclasses import dataclass

from src.services.booking.domain.time import TimeSlotEntity
from src.services.service_management.domain.entities.service import ServiceEntity
from src.shared.account.user import UserEntity
from src.services.booking.domain.address import Address
from src.services.booking.domain.reservation import Reservation


@dataclass
class AppointmentEntity:
    public_id: str
    selected_services: list[ServiceEntity]
    time_slot: TimeSlotEntity
    description: str
    client: UserEntity
    address: Address
    reservation: Reservation