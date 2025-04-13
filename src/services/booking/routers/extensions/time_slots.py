from src.services.booking.domain.time import TimeSlotEntity
from src.services.booking.schema.responses.time import GetTimeSlot, GetTimeSlots


class TimeEntityToGetTimeSlot:
    def __rmatmul__(self, time_slot: TimeSlotEntity):
        return GetTimeSlot(
            user_public_id=time_slot.service_provider.user_public_id,
            time_slot_public_id=time_slot.public_id,
            date=time_slot.date,
            start_time=time_slot.start_time,
            end_time=time_slot.end_time,
            is_booked=time_slot.is_booked
        )

class TimeEntityToGetTimeSlots:
    def __rmatmul__(self, time_slots: list[TimeSlotEntity]):
        return GetTimeSlots(time_slots=[time_slot @ TimeEntityToGetTimeSlot() for time_slot in time_slots])