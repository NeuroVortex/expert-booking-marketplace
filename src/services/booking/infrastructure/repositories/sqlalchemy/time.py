from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.booking.domain.time import TimeSlotEntity
from src.services.booking.infrastructure.models.time import TimeSlot
from src.services.booking.infrastructure.repositories.extensions.time import TimeSlotEntityToTimeSlot, \
    TimeSlotToTimeSlotEntity

from src.services.booking.infrastructure.repositories.time import ITimeSlotRepository
from src.shared.account.user import UserEntity


class TimeSlotRepositoryImpl(ITimeSlotRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def create_slot(self, time_slot: TimeSlotEntity) -> TimeSlotEntity:
        instance = time_slot @ TimeSlotEntityToTimeSlot()
        self.__session.add(instance)
        await self.__session.commit()
        await self.__session.refresh(instance)
        return instance @ TimeSlotToTimeSlotEntity()

    async def delete(self, time_slot_public_id: str) -> None:
        stmt = select(TimeSlot).where(TimeSlot.public_id == time_slot_public_id)
        instance = await self.__session.execute(stmt)
        await self.__session.delete(instance)

    async def get_slots_by_user(self, user: UserEntity) -> list[TimeSlotEntity]:
        stmt = select(TimeSlot).where(TimeSlot.user_id == user.id)
        result = await self.__session.execute(stmt)
        instances = result.scalars()
        return [instance @ TimeSlotToTimeSlotEntity() for instance in instances]

    async def booked(self, time_slot_public_id: str, booked: bool = True):
        stmt = update(TimeSlot).where(TimeSlot.public_id == time_slot_public_id).values(is_booked=booked)
        await self.__session.execute(stmt)
        await self.__session.commit()