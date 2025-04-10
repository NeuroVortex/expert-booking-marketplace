from abc import ABC, abstractmethod

from src.services.booking.domain.appointment import AppointmentEntity
from src.services.booking.domain.state import ReservationState
from src.shared.account.user import UserEntity


class Reservation(ABC):

    @abstractmethod
    async def create(self, appointment: AppointmentEntity):
        raise NotImplementedError

    @abstractmethod
    async def get_by_user(self, user: UserEntity):
        raise NotImplementedError

    @abstractmethod
    async def update(self, reservation):
        raise NotImplementedError

    @abstractmethod
    async def update_reservation_state(self, reservation_public_id: str, new_state: ReservationState):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, reservation):
        raise NotImplementedError
