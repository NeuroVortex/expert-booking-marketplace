from src.services.service_management.contract.service_dto import ServiceDto
from src.services.service_management.models.services import Service


class ToServiceDAO:
    def __rmatmul__(self, service: ServiceDto):
        return Service(
            parent_service_id=service.parent_service_id,
            name=service.name,
            profile=None,
            details={
                "description": service.description
            },
        )