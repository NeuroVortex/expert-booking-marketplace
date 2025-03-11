from src.infrastructure.db_manager.sql_alchemy.session import AsyncDatabaseSessionManager
from src.services.service_management.contract.service_dto import ServiceDto
from src.services.service_management.repositories.service import IServiceRepository
from kink import inject


@inject
class ServiceHandler:
    def __init__(self, service_repository: IServiceRepository):
        self.__service_repo: IServiceRepository = service_repository

    async def add_service(self, service: ServiceDto):
        async with AsyncDatabaseSessionManager() as session:
            return await self.__service_repo.service_repo(session).add(service)