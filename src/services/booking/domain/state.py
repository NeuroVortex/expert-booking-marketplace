from enum import IntEnum


class ReservationState(IntEnum):
    PENDING = 0
    CONFIRMED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4
    REJECTED = 5

