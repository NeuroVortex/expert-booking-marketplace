from src.shared.contract.appointment.address import Address
from src.services.booking.contract.user import User
from src.shared.contract.appointment.reservation import Reservation
from src.services.booking.routers.models.reservation import ReservationModel
from src.services.service_management.schemas.service import Service
from src.services.booking.domain.entities.appointment import AppointmentDto
from src.services.service_management.domain.entity.service_dto import ServiceDto


class ToServiceDto:
    def __rmatmul__(self, service_model: Service):
        return ServiceDto(name=service_model.name,
                          description=service_model.description,
                          parent_service_id=service_model.parentServiceId)

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