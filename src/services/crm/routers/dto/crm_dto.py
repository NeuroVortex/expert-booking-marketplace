from decimal import Decimal

from src.services.crm.contract.client import Client
from src.services.crm.contract.reservation import Reservation
from src.services.crm.routers.serializers.appointmentmodel import AppointmentModel
from src.services.sales.routers.serializer.service_model import ServiceModel
from src.shared.contract.crm.dto.appointment import AppointmentDto
from src.shared.contract.sales.dto.service_dto import ServiceDTO


class ToServiceDto:
    def __rmatmul__(self, service_model: ServiceModel):
        return ServiceDTO(title=service_model.Title,
                          description=service_model.Description,
                          price=Decimal(service_model.Price),
                          duration=service_model.Duration)

class ToAppointmentDto:
    def __rmatmul__(self, appointment: AppointmentModel):
        return AppointmentDto(selected_services=appointment.selectedServices,
                              description=appointment.description,
                              client=Client(name=appointment.client.name,
                                            family_name=appointment.client.family_name,
                                            email=appointment.client.email,
                                            phone=appointment.client.phone,
                                            address=appointment.client.address,
                                            national_code=appointment.client.national_code),
                              reservation=Reservation(datetime=appointment.datetime))