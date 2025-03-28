from src.services.account_management.models.user import User
from src.services.booking.domain.value_objects.address import Address
from src.services.booking.domain.value_objects.reservation import Reservation
from src.services.booking.routers.models.reservation import ReservationModel
from src.services.booking.routers.responses.response import Appointment
from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.schemas.requests.service import ServiceDto


class ToServiceDto:
    def __rmatmul__(self, entity: ServiceEntity):
        return ServiceDto(name=entity.name,
                          description=entity.details.description,
                          parent_service_id=entity.parent_service_id)

class ToReservationDto:
    def __rmatmul__(self, appointment: ReservationModel):
        return Appointment(selected_services=appointment.selectedServices,
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