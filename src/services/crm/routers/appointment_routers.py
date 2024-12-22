from datetime import datetime, date
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Body, Query

from src.services.crm.routers.helper.appointment_datetime import AppointmentDateTime
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
async def get_services(current_datetime: date | datetime = Query(str(datetime.now().isoformat()))) -> GetServices:

    try:
        date_times = AppointmentDateTime.generate(current_datetime)
        return date_times

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
