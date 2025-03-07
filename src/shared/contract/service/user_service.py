from datetime import timedelta
from decimal import Decimal
from typing import NamedTuple


class UserService(NamedTuple):
    user_id: int
    service_id: int
    price: Decimal
    duration: timedelta
