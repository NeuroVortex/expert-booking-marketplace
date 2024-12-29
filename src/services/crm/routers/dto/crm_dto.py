from decimal import Decimal

from src.services.sales.routers.serializer.service_model import ServiceModel
from src.shared.contract.sales.dto.service_dto import ServiceDTO


class ToServiceDto:
    def __rmatmul__(self, service_model: ServiceModel):
        return ServiceDTO(title=service_model.Title,
                          description=service_model.Description,
                          price=Decimal(service_model.Price),
                          duration=service_model.Duration)

class ToAppointmentDto:
    def __rmatmul__(self, service_model: ServiceModel):
        return