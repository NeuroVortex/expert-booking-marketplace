from sqlalchemy.ext.asyncio import AsyncSession

from src.services.account_management.domain.user import UserEntity
from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.infrastructure.repositories.user_service import IUserServiceRepository


class SQLAlchemyUserServiceRepository(IUserServiceRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__identity_map = dict()

    async def add(self, user: UserEntity, service: ServiceEntity):

        self.__session.add()

    async def remove(self, user_id, public_service_id):
        pass

    async def get_by_service_public_id(self, public_id) -> list[UserEntity]:
        pass

    async def get_by_user(self, user) -> list[ServiceEntity]:
        pass

    @classmethod
    def service_repo(cls, session: AsyncSession) -> 'IUserServiceRepository':
        return cls(session)