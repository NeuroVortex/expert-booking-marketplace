from src.infrastructure.db_manager.sql_alchemy.session import AsyncDatabaseSessionManager
from src.services.account_management.domain.user import UserEntity
from src.services.service_management.application.extensions.service import DtoToServiceEntity
from src.services.service_management.infrastructure.repositories.service import IServiceRepository
from kink import inject

from src.services.service_management.infrastructure.repositories.user_service import IUserServiceRepository
from src.services.service_management.schemas.requests.service import ServiceDto
from src.services.service_management.schemas.requests.user_service import UserServiceDto


@inject
class ServiceHandler:
    def __init__(self, service_repository: IServiceRepository, user_service_repository: IUserServiceRepository):
        self.__service_repo: IServiceRepository = service_repository
        self.__user_services_repo: IUserServiceRepository = user_service_repository

    async def add_service(self, service_dto: ServiceDto):
        async with AsyncDatabaseSessionManager() as session:
            parent = await self.__service_repo.service_repo(session).get_by_public_id(service_dto.parent_public_id)
            service = service_dto @ DtoToServiceEntity(parent.id)
            return await self.__service_repo.service_repo(session).add(service)

    async def delete_service(self, service_public_id: str):
        async with AsyncDatabaseSessionManager() as session:
            return await self.__service_repo.service_repo(session).delete(service_public_id)

    async def get_services(self, parent_public_id: str | None):
        async with AsyncDatabaseSessionManager() as session:
            return await self.__service_repo.service_repo(session).get_services(parent_public_id)

    async def get_bulk_services(self, parent_public_ids: list[str]):
        async with AsyncDatabaseSessionManager() as session:
            return await self.__service_repo.service_repo(session).get_bulk_services(parent_public_ids)

    def user_service_repo(self, session) -> IUserServiceRepository:
        return self.__user_services_repo.user_service_repo(session)

    def service_repo(self, session) -> IServiceRepository:
        return self.__service_repo.service_repo(session)