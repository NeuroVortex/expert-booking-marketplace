from enum import IntEnum


class TimePeriod(IntEnum):
    MORNING = 0 # 08:00 - 12:00
    AFTERNOON = 1 # 12:00 - 16:00
    EVENING = 2 # 16:00 - 20:00
    NIGHT = 3 # 20:00 - 24:00