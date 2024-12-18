from typing import NamedTuple


class Client(NamedTuple):
    name: str
    family_name: str
    email: str
    phone: str
    address: str
    national_code: str