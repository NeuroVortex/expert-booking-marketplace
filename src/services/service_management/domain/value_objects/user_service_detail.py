from decimal import Decimal
from typing import NamedTuple


class UserServiceDetail(NamedTuple):
    price: Decimal
    duration: str

    def to_dict(self):
        return {
            "price": str(self.price),
            "duration": self.duration,
        }

    @classmethod
    def from_dict(cls, other):
        return UserServiceDetail(price=Decimal(other["price"]), duration=other["duration"])