from sqlalchemy import select
from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.extensions.user_service import UserServicesToModel
from src.services.account_management.infrastructure.repositories.extensions.user_model import ToUser
from src.services.service_management.infrastructure.models.user_services import UserService
from src.services.service_management.infrastructure.repositories.extensions.to_service import ModelToServiceEntity
from src.services.service_management.infrastructure.repositories.extensions.to_user_service import \
    ModelToUserServiceEntity
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

    async def remove(self, user: UserEntity, services: list[ServiceEntity]):
        services_ids = [service.id for service in services]
        stmt = select(UserService).where(and_(UserService.user_id==user.id,
                                              UserService.service_id.in_(services_ids)))
        result = await self.__session.execute(stmt)
        await self.__session.delete(result.scalars())

    async def get(self, user_services_public_ids: list[str]) -> list[UserServiceEntity]:
        stmt = select(UserService).where(UserService.public_id.in_(user_services_public_ids))
        result = await self.__session.execute(stmt)
        instances = result.scalars()
        return [instance @ ModelToUserServiceEntity() for instance in instances]

    async def get_users_by_service_public_id(self, service: ServiceEntity) -> list[UserEntity]:
        stmt = select(UserService).where(UserService.service_id == service.id)
        instances = await self.__session.execute(stmt)
        results = instances.scalars()
        return [user_service.user @ ToUser() for user_service in results]

    async def get_by_user(self, user: UserEntity) -> list[ServiceEntity]:
        stmt = select(UserService).where(UserService.user_id==user.id)
        instances = await self.__session.execute(stmt)
        results = instances.scalars()
        return [user_service.service @ ModelToServiceEntity() for user_service in results]

    @classmethod
    def user_service_repo(cls, session: AsyncSession) -> 'IUserServiceRepository':
        return cls(session)