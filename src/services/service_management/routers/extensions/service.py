from src.services.service_management.domain.service_details import ServiceDetailsEntity
from src.services.service_management.domain.service_profile import ServiceProfileEntity
from src.services.service_management.schemas.service.service import Service
from src.services.service_management.domain.service import ServiceEntity


class ToServiceEntity:
    def __rmatmul__(self, service: Service | None):
        return ServiceEntity(name=service.name,
                             id=service.id,
                             public_id=service.public_id,
                             parent_service_id=service.parent_service_id,
                             details=ServiceDetailsEntity(**service.details),
                             profile=ServiceProfileEntity(**service.profile)) if service else None
