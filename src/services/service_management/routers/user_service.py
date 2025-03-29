from fastapi import APIRouter, HTTPException, status, Depends

from src.application.handler.user_service import UserServiceHandler
from src.services.service_management.application.handlers.service import ServiceHandler
from src.services.service_management.routers.dependencies.dependencies import Dependencies
from src.services.service_management.schemas.requests.user_service import UserServicesDto
from src.services.service_management.schemas.responses.service import ServiceAddedSuccessfully

user_service_router = APIRouter()

@user_service_router.post(path="/user-services", tags=["UserService"], status_code=status.HTTP_200_OK)
async def assing_service_to_user(user_services_dto: UserServicesDto, user_service_handler: UserServiceHandler =
                     Depends(Dependencies.service_handler)) -> ServiceAddedSuccessfully:
    try:
        public_id = await user_service_handler.assign_services_to_user(user_services_dto)
        return ServiceAddedSuccessfully(publicId=public_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_service_router.get(path="/user-services", tags=["UserService"], status_code=status.HTTP_200_OK)
async def get_users(service_public_id: str, service_handler: ServiceHandler =
                     Depends(Dependencies.service_handler)) -> ServiceAddedSuccessfully:
    try:
        public_id = await service_handler.get(service)
        return ServiceAddedSuccessfully(publicId=public_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

