from fastapi import APIRouter, HTTPException, status, Depends

from src.application.handler.user_service import UserServiceHandler
from src.schema.extensions.user import ToGetUser
from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.domain.entities.user_service import UserServiceEntity
from src.services.service_management.routers.dependencies.dependencies import Dependencies
from src.services.service_management.routers.extensions.service import ToGetServices
from src.services.service_management.routers.extensions.user_service import ToGetUserServices
from src.services.service_management.schemas.requests.user_service import UserServicesDto, UnassignUserServices
from src.services.service_management.schemas.responses.service import GetServices
from src.services.service_management.schemas.responses.user_service import GetServiceUsers, ServicesAssignSuccessfully, \
    ServicesUnassignSuccessfully
from src.shared.account.user import UserEntity

user_service_router = APIRouter()

@user_service_router.post(path="/user-services", status_code=status.HTTP_200_OK)
async def assign_service_to_user(user_services_dto: UserServicesDto, user_service_handler: UserServiceHandler =
                     Depends(Dependencies.user_service_handler)) -> ServicesAssignSuccessfully:
    try:
        await user_service_handler.assign_services_to_user(user_services_dto)
        return ServicesAssignSuccessfully()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@user_service_router.get(path="/user-services", status_code=status.HTTP_200_OK)
async def get_user_services(user_service_public_ids: list[str], user_service_handler: UserServiceHandler = Depends(Dependencies.user_service_handler)) -> GetServices:
    try:
        user_service: list[UserServiceEntity] = await user_service_handler.get_user_services(user_service_public_ids)
        return user_service @ ToGetUserServices()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@user_service_router.get(path="/user-services/users", status_code=status.HTTP_200_OK)
async def get_users(service_public_id: str, user_service_handler: UserServiceHandler =
                     Depends(Dependencies.user_service_handler)) -> GetServiceUsers:
    try:
        users: list[UserEntity] = await user_service_handler.get_users_by_service(service_public_id)
        return GetServiceUsers(users=[user @ ToGetUser() for user in users])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_service_router.get(path="/user-services/services", status_code=status.HTTP_200_OK)
async def get_services(user_public_id: str, user_service_handler: UserServiceHandler = Depends(Dependencies.user_service_handler)) -> GetServices:
    try:
        services: list[ServiceEntity] = await user_service_handler.get_services_by_user(user_public_id)
        return services @ ToGetServices()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@user_service_router.delete(path="/user-services", status_code=status.HTTP_200_OK)
async def unassigned_services(unassigned_request: UnassignUserServices, user_service_handler: UserServiceHandler = Depends(Dependencies.user_service_handler)) -> ServicesUnassignSuccessfully:
    try:
        await user_service_handler.unassigned_services(unassigned_request.public_user_id,
                                                       unassigned_request.services_public_ids)
        return ServicesUnassignSuccessfully()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))