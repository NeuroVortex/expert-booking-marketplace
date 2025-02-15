import random

from src.services.booking.routers.responses.response import Appointment


class AppointmentDateTime:

    @classmethod
    def generate(cls, current):
        date_times = []

        for i in range(9, 17):
            for j in range(0, 60, 30):
                date_times.append(Appointment(time=f"{i}".zfill(2) + ":" + f"{j}".zfill(2),
                                              available=0.3 > random.random()))

        return date_times