from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.domain.value_objects.service_details import ServiceDetails
from src.services.service_management.domain.value_objects.service_profile import ServiceProfile
from src.services.service_management.infrastructure.models.services import Service


class EntityToServiceModel:
    def __rmatmul__(self, service: ServiceEntity):
        return Service(
            parent_service_id=service.parent_service_id,
            name=service.name,
            profile=None,
            details=service.details._asdict()
        )

class ModelToServiceEntity:
    def __rmatmul__(self, service: Service) -> ServiceEntity:
        return ServiceEntity(name=service.name,
                             details=ServiceDetails(**service.details) if service.details else None,
                             id=service.id,
                             public_id=service.public_id,
                             parent_service_id=service.parent_service_id,
                             profile=ServiceProfile(**service.profile) if service.profile else None)
