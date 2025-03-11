from src.services.service_management.domain.service import ServiceEntity
from src.services.service_management.models.services import Service


class ToServiceDAO:
    def __rmatmul__(self, service: ServiceEntity):
        return Service(
            parent_service_id=service.parent_service_id,
            name=service.name,
            profile=None,
            details=service.details._asdict()
        )