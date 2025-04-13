from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from src.services.booking.domain.time import TimeSlotEntity
from src.shared.account.user import UserEntity


class ITimeSlotRepository(ABC):
    async def create_slot(self, time_slot: TimeSlotEntity) -> TimeSlotEntity:
        raise NotImplementedError

    async def delete(self, time_slot_public_id: str) -> None:
        raise NotImplementedError

    async def get_slots_by_user(self, user: UserEntity) -> list[TimeSlotEntity]:
        raise NotImplementedError

    async def get_slots_by_user_and_date(self, user: UserEntity, date_time: date) -> list[TimeSlotEntity]:
        raise NotImplementedError

    async def booked(self, time_slot_public_id: str):
        raise NotImplementedError

    @classmethod
    def time_repo(cls, session: AsyncSession) -> 'ITimeSlotRepository':
        raise NotImplementedError
