from typing import Annotated

from fastapi import APIRouter, HTTPException, status, UploadFile, Depends

from src.services.service_management.application.handlers.service import ServiceHandler
from src.services.service_management.dependencies.dependencies import Dependencies
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

        serialized_services = GetServices(services=[GetService(public_id=service.public_id,
                                          title=service.name,
                                          description=service.details.description,
                                          is_active=True) for service in services])
        return serialized_services




        # services = [{"id": 1, "title": 'HVAC', "duration": "30", "description": "HVAC" ,
        #              "price": "30", "selected": False},
        #             {"id": 2, "title": 'Bathroom Maintenance', "duration": "120", "description": "Bathroom Maintenance",
        #              "price": "100", "selected": False},
        #             {"id": 3, "title": 'Plumbing', "duration": "45", "description": "Plumbing",
        #              "price": "35", "selected": False},
        #             {"id": 4, "title": 'Replace Windows', "duration": "60", "description": "Replace Windows",
        #              "price": "45", "selected": False},
        #             {"id": 5, "title": 'Landscaping', "duration": "60", "description": "Landscaping",
        #              "price": "70", "selected": False},
        #             {"id": 6, "title": 'Clean dryer exhaust duct', "duration": "60", "description": "Clean dryer exhaust duct",
        #              "price": "70", "selected": False}]


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

