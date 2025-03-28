from decimal import Decimal

from kink import inject

from src.services.account_management.domain.user import UserEntity
from src.services.account_management.repositories.user import IUserRepository
from src.services.service_management.application.handlers.service import ServiceHandler
from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.domain.entities.user_service import UserServiceEntity
from src.services.service_management.domain.value_objects.user_service_detail import UserServiceDetail
from src.services.service_management.infrastructure.repositories.user_service import IUserServiceRepository
from src.services.service_management.schemas.requests.user_service import UserServicesDto, UserServiceDto


@inject
class UserServiceHandler:
    def __init__(self, user_repository: IUserRepository,
                 user_service_repository: IUserServiceRepository):
        self.__service_handler = ServiceHandler()
        self.__user_service_repo: IUserServiceRepository = user_service_repository
        self.__user_repo: IUserRepository = user_repository

    async def assign_services_to_user(self, user_service_dto: UserServicesDto):
        user: UserEntity = await self.__user_repo.get_by_user_public_id(user_service_dto.public_user_id)
        services_public_ids = [service.public_id for service in user_service_dto.services]
        services: list[ServiceEntity] = await self.__service_handler.get_bulk_services(services_public_ids)
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

        await self.__user_service_repo.add(user_services)