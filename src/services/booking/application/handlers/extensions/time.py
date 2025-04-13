from src.services.booking.domain.time import TimeSlotEntity
from src.services.booking.helpers.time import TimePeriodFinder
from src.services.booking.schema.time import TimeSlotDto
from src.shared.account.user import UserEntity


class DtoToTimeSlot:
    def __init__(self, user: UserEntity):
        self.user = user

    def __rmatmul__(self, time_slot_dto: TimeSlotDto) -> TimeSlotEntity:
        return TimeSlotEntity(
            service_provider=self.user,
            date=time_slot_dto.date,
            start_time=time_slot_dto.start_time,
            end_time=time_slot_dto.end_time,
            period=TimePeriodFinder.get(time_slot_dto.start_time)
        )