from sqlalchemy.ext.asyncio import AsyncSession

from src.application.extensions.user_service import UserServicesToModel
from src.shared.account.user import UserEntity
from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.domain.entities.user_service import UserServiceEntity
from src.services.service_management.infrastructure.repositories.user_service import IUserServiceRepository


class SQLAlchemyUserServiceRepository(IUserServiceRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__identity_map = dict()

    async def add(self, user_services: list[UserServiceEntity]):
        instances = [user_service @ UserServicesToModel() for user_service in user_services]
        self.__session.add_all(instances)
        await self.__session.commit()

    async def remove(self, user_id, public_service_id):
        pass

    async def get_by_service_public_id(self, public_id) -> list[UserEntity]:
        pass

    async def get_by_user(self, user) -> list[ServiceEntity]:
        pass

    @classmethod
    def user_service_repo(cls, session: AsyncSession) -> 'IUserServiceRepository':
        return cls(session)