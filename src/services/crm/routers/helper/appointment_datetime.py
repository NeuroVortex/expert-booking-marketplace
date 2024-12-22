import random


class AppointmentDateTime:

    @classmethod
    def generate(cls, current):
        date_times = []

        for i in range(9, 17):
            for j in range(0, 60, 30):
                date_times.append({"time": f"{i}".zfill(2) + ":" + f"{j}".zfill(2), "available": 0.3 > random.random()})