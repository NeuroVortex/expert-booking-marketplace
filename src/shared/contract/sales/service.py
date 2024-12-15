from typing import NamedTuple


class Service(NamedTuple):
    id: int
    name: str
    duration: int
    price: int
    selected: bool
