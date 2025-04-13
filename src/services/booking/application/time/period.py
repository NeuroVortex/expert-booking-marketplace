from datetime import time

from src.services.booking.domain.period import TimePeriod


class TimePeriodFinder:

    @classmethod
    def get(cls, start_time: time):
        hour = start_time.hour
        if 8 <= hour < 12:
            return TimePeriod.MORNING
        elif 12 <= hour < 16:
            return TimePeriod.AFTERNOON
        elif 16 <= hour < 20:
            return TimePeriod.EVENING
        else:
            return TimePeriod.NIGHT