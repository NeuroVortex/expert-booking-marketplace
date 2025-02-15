from datetime import datetime, date
from pydantic import BaseModel, ValidationError

from fastapi import APIRouter, HTTPException, status, Query

from src.services.booking.routers.dto.crm_dto import ToReservationDto
from src.services.booking.routers.helper.appointment_datetime import AppointmentDateTime
from src.services.booking.routers.responses.response import Schedules
from src.services.booking.routers.models.reservation import ReservationModel

appointment_router = APIRouter()


@appointment_router.post(path="/add", tags=["Crm"], status_code=status.HTTP_200_OK)
async def set_1_appointment(appointment: dict) -> int:
    print(appointment)
    try:
        appointment_dto = appointment @ ToReservationDto()
        return 1

    except ValidationError as e:
        print(e)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@appointment_router.get(path="", tags=["ReservationModel"], status_code=status.HTTP_200_OK)
async def get_schedules(current_datetime: date | datetime = Query(str(datetime.now().isoformat()))) -> Schedules:

    try:
        date_times = AppointmentDateTime.generate(current_datetime)
        return Schedules(schedules=date_times)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
