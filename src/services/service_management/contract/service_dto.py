from  typing import NamedTuple


class ServiceDto(NamedTuple):
    name: str
    description: str
    parent_service_id: int | None = None
