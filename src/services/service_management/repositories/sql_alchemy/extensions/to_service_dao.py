from src.services.service_management.contract.service_dto import ServiceDto
from src.services.service_management.schemas.services import ServiceSchema


class ToServiceDAO:
    def __rmatmul__(self, service: ServiceDto):
        return ServiceSchema(
            parent_service_id=service.parent_service_id,
            name=service.name,
            profile=None,
            details={
                "description": service.description
            },
        )