from fastapi import APIRouter, HTTPException, status, Depends

from src.services.service_management.dependencies.dependencies import Dependencies
from src.services.service_management.handlers.service import ServiceHandler
from src.services.service_management.schemas.responses.service import ServiceAddedSuccessfully, GetServices, GetService


service_router = APIRouter()


@service_router.post(path="/user-services", tags=["UserService"], status_code=status.HTTP_200_OK)
async def get_users(parent_public_id: str, service_handler: ServiceHandler =
                     Depends(Dependencies.service_handler)) -> ServiceAddedSuccessfully:
    try:
        public_id = await service_handler.add_service(service)
        return ServiceAddedSuccessfully(publicId=public_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

