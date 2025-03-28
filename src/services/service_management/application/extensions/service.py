from src.services.service_management.domain.value_objects.service_details import ServiceDetails
from src.services.service_management.schemas.requests.service import ServiceDto
from src.services.service_management.domain.entities.service import ServiceEntity


class DtoToServiceEntity:
    def __init__(self, parent_id: int | None = None):
        self.__parent_id = parent_id

    def __rmatmul__(self, service: ServiceDto | None):
        return ServiceEntity(name=service.name,
                             parent_service_id=self.__parent_id,
                             details=ServiceDetails(description=service.description)) if service else None
