from src.services.service_management.domain.entities.service import ServiceEntity
from dataclasses import asdict

class ToUpdatedService:
    def __rmatmul__(self, entity: ServiceEntity) -> dict:
        return {k: v for k, v in asdict(entity).items()}
