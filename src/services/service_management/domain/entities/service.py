from dataclasses import dataclass

from src.services.service_management.domain.value_objects.service_details import ServiceDetails
from src.services.service_management.domain.value_objects.service_profile import ServiceProfile


@dataclass
class ServiceEntity:
    name: str
    details: ServiceDetails
    id: int | None = None
    public_id: str | None = None
    parent_service_id: int | None = None
    profile: ServiceProfile | None = None
