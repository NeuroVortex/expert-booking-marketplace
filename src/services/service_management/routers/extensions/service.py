from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.schemas.responses.service import GetService, GetServices


class ToGetService:
    def __rmatmul__(self, service: ServiceEntity):
        return GetService(public_id=service.public_id,
                          title=service.name,
                          description=service.details.description,
                          is_active=True)

class ToGetServices:
    def __rmatmul__(self, services: list[ServiceEntity]):
        return GetServices(services=[service @ ToGetService() for service in services])