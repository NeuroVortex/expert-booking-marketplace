from datetime import date

from src.infrastructure.db_manager.sql_alchemy.session import AsyncDatabaseSessionManager
from src.services.account_management.infrastructure.repositories.user import IUserRepository
from src.services.booking.domain.time import TimeSlotEntity
from src.services.booking.handlers.exceptions.time import TimeSlotConflictException
from src.services.booking.handlers.extensions.time import DtoToTimeSlot
from src.services.booking.infrastructure.repositories.time import ITimeSlotRepository
from src.services.booking.schema.time import TimeSlotDto
from src.shared.account.user import UserEntity


class TimeSlotHandler:
    def __init__(self, time_repo: ITimeSlotRepository, user_repo: IUserRepository):
        self.__time_repo = time_repo
        self.__user_repo = user_repo

    async def create_time_slot(self, time_slot_dto: TimeSlotDto):
        async with AsyncDatabaseSessionManager() as session:
            user: UserEntity = await self.__user_repo.user_repo(session).get_by_user_public_id(time_slot_dto.user_public_id)
            slot_entity = time_slot_dto @ DtoToTimeSlot(user)
            time_slots = await self.__time_repo.time_repo(session).get_slots_by_user_and_date(user, time_slot_dto.date)
            eq_time_slot = next((time_slot for time_slot in time_slots if time_slot == slot_entity), False)
            if not eq_time_slot:
                await self.__time_repo.time_repo(session).create_slot(time_slot_dto @ DtoToTimeSlot(user))

            else:
                raise TimeSlotConflictException()

    async def get_time_slots_by_user_and_date(self, user_public_id: str, day: date) -> list[TimeSlotEntity]:
        async with AsyncDatabaseSessionManager() as session:
            user: UserEntity = await self.__user_repo.user_repo(session).get_by_user_public_id(user_public_id)
            time_slots: list[TimeSlotEntity] = await self.__time_repo.time_repo(session).get_slots_by_user_and_date(
                user, day)
            return time_slots

    async def delete(self, time_slot_public_id: str):
        async with AsyncDatabaseSessionManager() as session:
            await self.__time_repo.time_repo(session).delete(time_slot_public_id)

    async def book_time(self, time_slot_public_id: str):
        async with AsyncDatabaseSessionManager() as session:
            await self.__time_repo.time_repo(session).booked(time_slot_public_id)