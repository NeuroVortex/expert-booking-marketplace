from typing import Annotated

from fastapi import APIRouter, HTTPException, status, UploadFile, Depends

from src.services.service_management.application.handlers.service import ServiceHandler
from src.services.service_management.routers.dependencies.dependencies import Dependencies
from src.services.service_management.routers.extensions.service import ToGetService, ToGetServices
from src.services.service_management.schemas.responses.service import ServiceAddedSuccessfully, GetServices, GetService, \
    ServiceDeletedSuccessfully
from src.services.service_management.schemas.requests.service import ServiceDto

service_router = APIRouter()


@service_router.post(path="", status_code=status.HTTP_200_OK)
async def add_service(service: ServiceDto, service_handler: ServiceHandler =
                     Depends(Dependencies.service_handler)) -> ServiceAddedSuccessfully:
    try:
        public_id = await service_handler.add_service(service)
        return ServiceAddedSuccessfully(publicId=public_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@service_router.post(path="/upload", status_code=status.HTTP_200_OK)
async def upload_service_photo(service_public_id: str, file: Annotated[UploadFile, None]) -> ServiceAddedSuccessfully:
    try:

        return ServiceAddedSuccessfully(id=1)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@service_router.get(path="", status_code=status.HTTP_200_OK)
async def get_services(parent_public_id: str | None = None, service_handler: ServiceHandler =
                     Depends(Dependencies.service_handler)) -> GetServices:
    try:
        print(parent_public_id)
        services = await service_handler.get_services(parent_public_id)
        return services @ ToGetServices()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@service_router.delete(path="", status_code=status.HTTP_200_OK)
async def delete_service(service_public_id: str, service_handler: ServiceHandler =
                     Depends(Dependencies.service_handler)) -> ServiceDeletedSuccessfully:
    try:
            await service_handler.delete_service(service_public_id)
            return ServiceDeletedSuccessfully()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

