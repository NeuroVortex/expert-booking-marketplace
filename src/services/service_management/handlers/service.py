from src.infrastructure.db_manager.sql_alchemy.session import AsyncDatabaseSessionManager
from src.services.service_management.repositories.service import IServiceRepository
from kink import inject

from src.services.service_management.schemas.service import Service


@inject
class ServiceHandler:
    def __init__(self, service_repository: IServiceRepository):
        self.__service_repo: IServiceRepository = service_repository

    async def add_service(self, service: Service):
        async with AsyncDatabaseSessionManager() as session:
            return await self.__service_repo.service_repo(session).add(service)


    async def delete_service(self, service_id: str):
        async with AsyncDatabaseSessionManager() as session:
            return await self.__service_repo.service_repo(session).delete(service_id)