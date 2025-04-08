from decimal import Decimal

from kink import inject

from src.infrastructure.db_manager.sql_alchemy.session import AsyncDatabaseSessionManager
from src.services.service_management.infrastructure.repositories.service import IServiceRepository
from src.shared.account.user import UserEntity
from src.services.account_management.infrastructure.repositories.user import IUserRepository
from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.domain.entities.user_service import UserServiceEntity
from src.services.service_management.domain.value_objects.user_service_detail import UserServiceDetail
from src.services.service_management.infrastructure.repositories.user_service import IUserServiceRepository
from src.services.service_management.schemas.requests.user_service import UserServicesDto, UserServiceDto


@inject
class UserServiceHandler:
    def __init__(self, user_repository: IUserRepository,
                 service_repository: IServiceRepository,
                 user_service_repository: IUserServiceRepository):
        self.__service_repo: IServiceRepository = service_repository
        self.__user_service_repo: IUserServiceRepository = user_service_repository
        self.__user_repo: IUserRepository = user_repository

    async def assign_services_to_user(self, user_service_dto: UserServicesDto):
        async with AsyncDatabaseSessionManager() as session:
            user: UserEntity = await self.__user_repo.user_repo(session).get_by_user_public_id(user_service_dto.public_user_id)
            services_public_ids = [service.public_id for service in user_service_dto.services]
            services: list[ServiceEntity] = await self.__service_repo.service_repo(session).get_bulk_services(services_public_ids)
        user_services = []
        for service in services:
            service_dto: UserServiceDto = next(
                (dto for dto in user_service_dto.services if dto.public_id == service.public_id),
                False
            )

            if service_dto:
                user_services.append(
                    UserServiceEntity(user=user,
                                      service=service,
                                      detail=UserServiceDetail(price=Decimal(service_dto.price),
                                                               duration=str(service_dto.duration))
                )
                )

        await self.__user_service_repo.user_service_repo(session).add(user_services)

    async def get_user_services(self, user_service_public_id: list[str]) -> list[UserServiceEntity]:
        async with AsyncDatabaseSessionManager() as session:
            user_services: list[UserServiceEntity] = await self.__user_service_repo.user_service_repo(session).get(
                user_service_public_id)
            return user_services

    async def get_services_by_user(self, user_public_id: str) -> list[ServiceEntity]:
        async with AsyncDatabaseSessionManager() as session:
            user: UserEntity = await self.__user_repo.user_repo(session).get_by_user_public_id(user_public_id)
            services: list[ServiceEntity] = await self.__user_service_repo.user_service_repo(session).get_by_user(user)
            return services

    async def get_users_by_service(self, service_public_id: str) -> list[UserEntity]:
        async with AsyncDatabaseSessionManager() as session:
            service: ServiceEntity = await self.__service_repo.service_repo(session).get_by_public_id(service_public_id)
            users: list[UserEntity] = await self.__user_service_repo.user_service_repo(
                session).get_users_by_service_public_id(service)
            return users

    async def unassigned_services(self, user_public_id: str, services_public_ids: list[str]):
        async with AsyncDatabaseSessionManager() as session:
            user: UserEntity = await self.__user_repo.user_repo(session).get_by_user_public_id(user_public_id)
            services: list[ServiceEntity] = await self.__service_repo.service_repo(session).get_bulk_services(
                services_public_ids)
            await self.__user_service_repo.user_service_repo(session).remove(user, services)
