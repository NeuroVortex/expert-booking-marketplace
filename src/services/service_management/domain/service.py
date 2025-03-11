from dataclasses import dataclass

from src.services.service_management.domain.service_details import ServiceDetailsEntity
from src.services.service_management.domain.service_profile import ServiceProfileEntity


@dataclass
class ServiceEntity:
    name: str
    details: ServiceDetailsEntity
    id: int | None = None
    public_id: str | None = None
    parent_service_id: int | None = None
    profile: ServiceProfileEntity | None = None
    children: list["ServiceEntity"] | None = None