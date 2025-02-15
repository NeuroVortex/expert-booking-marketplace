from typing import NamedTuple


class User(NamedTuple):
    first_name: str
    last_name: str
    email: str
    phone: str
    identifier: str