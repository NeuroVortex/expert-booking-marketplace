from src.services.account_management.infrastructure.models.user import User
from src.services.booking.domain.address import Address
from src.services.booking.domain.reservation import Reservation
from src.services.booking.routers.responses.response import Appointment
from src.services.booking.schema.reservation import ReservationDto


class DtoToReservationEntity:
    def __rmatmul__(self, appointment: ReservationDto):
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