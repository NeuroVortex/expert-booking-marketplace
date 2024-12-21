from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status

from src.services.sales.routers.dto.service_extensions import ToServiceDto
from src.services.sales.routers.response.responses import ServiceAddedSuccessfully, GetServices, GetService
from src.services.sales.routers.serializer.service_model import ServiceModel

appointment_router = APIRouter()


@appointment_router.post(path="/add", tags=["crm"], status_code=status.HTTP_200_OK)
async def add_service(service: ServiceModel) -> ServiceAddedSuccessfully:
    try:
        service_dto = service @ ToServiceDto()
        return ServiceAddedSuccessfully(id=1)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@appointment_router.get(path="", tags=["service"], status_code=status.HTTP_200_OK)
async def get_services(current: str) -> GetServices:
    current_datetime = datetime.fromisoformat(current)
    date = current_datetime.date()
    try:
        date_times = [{"time": date, "available": True},
                      {"time": datetime.time(), "available": True},
                      {"time": datetime.time(), "available": False},
                      {"time": datetime.time(), "available": True},
                      {"time": datetime.time(), "available": False},
                      {"time": datetime.time(), "available": True}]

        serialized_services = GetServices(services=[GetService(id=service["id"],
                    title=service["title"],
                    description=service["description"],
                    duration=service["duration"],
                    price=service["price"],
                    selected=service["selected"]) for service in services])

        return serialized_services

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
