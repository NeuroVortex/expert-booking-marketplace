import uuid
from src.shared.contract.media.photo import Photo
from src.shared.contract.service.details import ServiceDetails
from typing import NamedTuple


class Service(NamedTuple):
    service_id: int
    name: str
    details: ServiceDetails
    parent_service_id: int | None
    slug: str = uuid.uuid4()
    photo: Photo | None = None
    children: list["Service"] | None = None
