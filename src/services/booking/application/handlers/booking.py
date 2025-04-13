from src.infrastructure.db_manager.sql_alchemy.session import AsyncDatabaseSessionManager
from src.services.account_management.infrastructure.repositories.user import IUserRepository
from src.services.booking.domain.appointment import AppointmentEntity
from src.services.booking.infrastructure.repositories.reservation import IReservationRepository
from src.services.booking.infrastructure.repositories.time import ITimeSlotRepository
from src.services.booking.routers.extensions.reservation import DtoToReservationEntity
from src.services.booking.schema.reservation import ReservationDto


class BookingHandler:
    def __init__(self, time_repo: ITimeSlotRepository, user_repo: IUserRepository, reservation_repo: IReservationRepository):
        self.__time_repo = time_repo
        self.__user_repo = user_repo
        self.__reservation_repo = reservation_repo

    async def reserve(self, reservation_dto: ReservationDto):
        async with AsyncDatabaseSessionManager() as session:
            reservation: AppointmentEntity = await self.__reservation_repo.reservation_repo(session).create(reservation_dto @ DtoToReservationEntity())
