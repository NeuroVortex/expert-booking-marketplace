from datetime import timedelta
from decimal import Decimal
from typing import NamedTuple

from src.services.service_management.domain.service import ServiceEntity


class UserService(NamedTuple):
    user_id: int
    service: ServiceEntity
    price: Decimal
    duration: timedelta
