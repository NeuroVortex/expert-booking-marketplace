from src.services.service_management.routers.serializer.service_model import ServiceModel
from src.shared.contract.service.details import ServiceDetails
from src.shared.contract.service.service import Service


class ToService:
    def __rmatmul__(self, service_model: ServiceModel):
        return Service(name=service_model.Title,
                       details=ServiceDetails(description=service_model.Description))
