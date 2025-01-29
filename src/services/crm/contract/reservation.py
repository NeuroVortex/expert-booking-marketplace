from typing import NamedTuple
from datetime import datetime


class Reservation(NamedTuple):
    datetime: datetime
    reserved_phone: str
