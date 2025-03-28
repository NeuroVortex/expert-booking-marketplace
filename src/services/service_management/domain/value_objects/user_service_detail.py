from datetime import timedelta
from decimal import Decimal
from typing import NamedTuple


class UserServiceDetail(NamedTuple):
    price: Decimal
    duration: str
