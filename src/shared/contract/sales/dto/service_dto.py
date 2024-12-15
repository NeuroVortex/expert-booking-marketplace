from decimal import Decimal
from  typing import NamedTuple


class ServiceDTO(NamedTuple):
    title: str
    description: str
    duration: int
    price: Decimal