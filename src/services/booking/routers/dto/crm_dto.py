from decimal import Decimal

from src.shared.contract.appointment.address import Address
from src.services.booking.contract.user import User
from src.shared.contract.appointment.reservation import Reservation
from src.services.booking.routers.models.reservation import ReservationModel
from src.services.service_management.routers.serializer.service_model import ServiceModel
from src.services.booking.contract.appointment import AppointmentDto
from src.services.service_management.contract.service_dto import ServiceDTO


class ToServiceDto:
    def __rmatmul__(self, service_model: ServiceModel):
        return ServiceDTO(title=service_model.Title,
                          description=service_model.Description,
                          price=Decimal(service_model.Price),
                          duration=service_model.Duration)

class ToReservationDto:
    def __rmatmul__(self, appointment: ReservationModel):
        return AppointmentDto(selected_services=appointment.selectedServices,
                              description=appointment.description,
                              client=User(first_name=appointment.client.name,
                                            last_name=appointment.client.family_name,
                                            email=appointment.client.email,
                                            phone=appointment.client.phone,
                                            identifier=appointment.client.national_code),
                              reservation=Reservation(datetime=appointment.datetime,
                                                      reserved_phone=appointment.client.phone),
                              address=Address(city='',
                                             province='',
                                             street='',
                                             number='',
                                             zip_code=''))