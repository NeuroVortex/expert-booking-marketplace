from fastapi import APIRouter, HTTPException, status, Depends

from src.application.handler.user_service import UserServiceHandler
from src.schema.extensions.user import ToGetUser
from src.services.service_management.routers.dependencies.dependencies import Dependencies
from src.services.service_management.schemas.requests.user_service import UserServicesDto
from src.services.service_management.schemas.responses.user_service import GetServiceUsers, ServicesAssignSuccessfully
from src.shared.account.user import UserEntity

user_service_router = APIRouter()

@user_service_router.post(path="/user-services", tags=["UserService"], status_code=status.HTTP_200_OK)
async def assign_service_to_user(user_services_dto: UserServicesDto, user_service_handler: UserServiceHandler =
                     Depends(Dependencies.user_service_handler)) -> ServicesAssignSuccessfully:
    try:
        await user_service_handler.assign_services_to_user(user_services_dto)
        return ServicesAssignSuccessfully()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_service_router.get(path="/user-services", tags=["UserService"], status_code=status.HTTP_200_OK)
async def get_users(service_public_id: str, user_service_handler: UserServiceHandler =
                     Depends(Dependencies.user_service_handler)) -> GetServiceUsers:
    try:
        users: list[UserEntity] = await user_service_handler.get_users_by_service(service_public_id)
        return GetServiceUsers(users=[user @ ToGetUser() for user in users])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

