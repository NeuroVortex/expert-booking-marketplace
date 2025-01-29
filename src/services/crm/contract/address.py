from typing import NamedTuple


class Address(NamedTuple):
    city: str
    province: str
    street: str
    number: str
    zip_code: str
