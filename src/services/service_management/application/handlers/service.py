from src.infrastructure.db_manager.sql_alchemy.session import AsyncDatabaseSessionManager
from src.services.service_management.application.extensions.service import DtoToServiceEntity
from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.domain.value_objects.service_details import ServiceDetails
from src.services.service_management.infrastructure.repositories.service import IServiceRepository
from kink import inject

from src.services.service_management.schemas.service.service import ServiceDto


@inject
class ServiceHandler:
    def __init__(self, service_repository: IServiceRepository):
        self.__service_repo: IServiceRepository = service_repository

    async def add_service(self, service_dto: ServiceDto):
        async with AsyncDatabaseSessionManager() as session:
            parent = await self.__service_repo.service_repo(session).get_by_public_id(service_dto.parent_public_id)
            service = service_dto @ DtoToServiceEntity(parent.id)
            return await self.__service_repo.service_repo(session).add(service)

    async def delete_service(self, service_id: str):
        async with AsyncDatabaseSessionManager() as session:
            return await self.__service_repo.service_repo(session).delete(service_id)

    async def get_services(self, parent_public_id: str | None):
        async with AsyncDatabaseSessionManager() as session:
            return await self.__service_repo.service_repo(session).get_services(parent_public_id)