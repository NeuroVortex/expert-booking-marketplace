from src.services.account_management.infrastructure.repositories.extensions.user import ToUser
from src.services.booking.domain.period import TimePeriod
from src.services.booking.domain.time import TimeSlotEntity
from src.services.booking.infrastructure.models.time import TimeSlot


class TimeSlotEntityToTimeSlot:
    def __rmatmul__(self, time_slot: TimeSlotEntity):
        return TimeSlot(
            user_id=time_slot.service_provider.id,
            date=time_slot.date,
            start_time=time_slot.start_time,
            end_time=time_slot.end_time,
            period=time_slot.period.name,
            is_booked=time_slot.is_booked
        )


class TimeSlotToTimeSlotEntity:
    def __rmatmul__(self, time_slot: TimeSlot):
        return TimeSlotEntity(
            service_provider=time_slot.user @ ToUser(),
            date=time_slot.date,
            start_time=time_slot.start_time,
            end_time=time_slot.end_time,
            period=TimePeriod[time_slot.period],
            id=time_slot.id,
            public_id=time_slot.public_id,
            is_booked=time_slot.is_booked
        )