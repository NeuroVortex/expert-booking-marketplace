from src.services.booking.handlers.booking import BookingHandler
from src.services.booking.handlers.time import TimeSlotHandler


class Dependencies:

    Dependencies = None

    def __init__(self):
        Dependencies.Dependencies = self

    @classmethod
    def booking_handler(cls):
        return BookingHandler()

    @classmethod
    def time_slot_handler(cls):
        return TimeSlotHandler()