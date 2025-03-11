from typing import Annotated

from fastapi import APIRouter, HTTPException, status, UploadFile, Depends

from src.services.booking.routers.dto.crm_dto import ToServiceDto
from src.services.service_management.contract.service_dto import ServiceDto
from src.services.service_management.dependencies.dependencies import Dependencies
from src.services.service_management.handlers.service import ServiceHandler
from src.services.service_management.routers.response.responses import ServiceAddedSuccessfully, GetServices, GetService
from src.services.service_management.routers.serializer.service_model import ServiceModel

service_router = APIRouter()


@service_router.post(path="/add", tags=["Service"], status_code=status.HTTP_200_OK)
async def add_service(service: ServiceModel, service_handler: ServiceHandler =
                     Depends(Dependencies.service_handler)) -> ServiceAddedSuccessfully:
    try:
        service: ServiceDto = service @ ToServiceDto()
        public_id = await service_handler.add_service(service)
        return ServiceAddedSuccessfully(publicId=public_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@service_router.post(path="/upload", tags=["Service"], status_code=status.HTTP_200_OK)
async def upload_service_photo(service_slug: str, file: Annotated[UploadFile, None]) -> ServiceAddedSuccessfully:
    try:

        return ServiceAddedSuccessfully(id=1)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@service_router.get(path="", tags=["Service"], status_code=status.HTTP_200_OK)
async def get_services() -> GetServices:
    try:
        services = [{"id": 1, "title": 'HVAC', "duration": "30", "description": "HVAC" ,
                     "price": "30", "selected": False},
                    {"id": 2, "title": 'Bathroom Maintenance', "duration": "120", "description": "Bathroom Maintenance",
                     "price": "100", "selected": False},
                    {"id": 3, "title": 'Plumbing', "duration": "45", "description": "Plumbing",
                     "price": "35", "selected": False},
                    {"id": 4, "title": 'Replace Windows', "duration": "60", "description": "Replace Windows",
                     "price": "45", "selected": False},
                    {"id": 5, "title": 'Landscaping', "duration": "60", "description": "Landscaping",
                     "price": "70", "selected": False},
                    {"id": 6, "title": 'Clean dryer exhaust duct', "duration": "60", "description": "Clean dryer exhaust duct",
                     "price": "70", "selected": False}]

        serialized_services = GetServices(services=[GetService(id=service["id"],
                    title=service["title"],
                    description=service["description"],
                    duration=service["duration"],
                    price=service["price"],
                    selected=service["selected"]) for service in services])

        return serialized_services

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
