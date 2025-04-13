from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError
from datetime import date

from src.services.booking.dependencies.dependencies import Dependencies
from src.services.booking.domain.time import TimeSlotEntity
from src.services.booking.handlers.time import TimeSlotHandler
from src.services.booking.routers.extensions.time_slots import TimeEntityToGetTimeSlots
from src.services.booking.schema.time import TimeSlotDto

time_router = APIRouter()


@time_router.post("/time_slots")
async def add_time_slot(time_slot: TimeSlotDto, time_slot_handler: TimeSlotHandler = Depends(Dependencies.time_slot_handler)):
    try:
        await time_slot_handler.create_time_slot(time_slot)

    except ValidationError as e:
        HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@time_router.get("/{user_public_id}/time_slots")
async def add_time_slot(user_public_id: str, day: date, time_slot_handler: TimeSlotHandler = Depends(Dependencies.time_slot_handler)):
    try:
        time_slots: list[TimeSlotEntity] = await time_slot_handler.get_time_slots_by_user_and_date(user_public_id, day)
        return time_slots @ TimeEntityToGetTimeSlots()

    except ValidationError as e:
        HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@time_router.delete("/time_slots")
async def remove_time_slot(time_slot_public_id: str, time_slot_handler: TimeSlotHandler = Depends(Dependencies.time_slot_handler)):
    try:
        await time_slot_handler.delete(time_slot_public_id)

    except ValidationError as e:
        HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))