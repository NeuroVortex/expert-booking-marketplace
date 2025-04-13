from datetime import datetime, date

from fastapi.params import Depends
from pydantic import BaseModel, ValidationError

from fastapi import APIRouter, HTTPException, status, Query

from src.services.booking.dependencies.dependencies import Dependencies
from src.services.booking.handlers.booking import BookingHandler
from src.services.booking.routers.extensions.reservation import DtoToReservationEntity
from src.services.booking.routers.helper.appointment_datetime import AppointmentDateTime
from src.services.booking.schema.reservation import ReservationDto

appointment_router = APIRouter()


@appointment_router.post(path="/add", status_code=status.HTTP_200_OK)
async def reserve(appointment: ReservationDto, handler: BookingHandler = Depends(Dependencies.booking_handler)) -> str:

    try:
        appointment = appointment


    except ValidationError as e:
        HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@appointment_router.get(path="", tags=["ReservationModel"], status_code=status.HTTP_200_OK)
async def get_appointments(current_datetime: date | datetime = Query(str(datetime.now().isoformat()))) -> list[GetAppointment]:

    try:
        date_times = AppointmentDateTime.generate(current_datetime)
        return Schedules(schedules=date_times)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
