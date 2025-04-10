from datetime import datetime, timedelta


class TimeSlotGenerator:

    @classmethod
    def generate(cls, date, slot_length_minutes=90):
        base_time = datetime.combine(date, datetime.strptime("08:00", "%H:%M").time())
        periods = [("Morning", "08:00", "12:00"), ("Afternoon", "12:00", "16:00"), ("Evening", "16:00", "20:00")]

        slots = []
        for period, start_str, end_str in periods:
            start = datetime.strptime(start_str, "%H:%M").time()
            end = datetime.strptime(end_str, "%H:%M").time()
            curr = datetime.combine(date, start)
            while curr.time() < end:
                slots.append({
                    "date": date,
                    "start_time": curr.time(),
                    "end_time": (curr + timedelta(minutes=slot_length_minutes)).time(),
                    "period": period
                })
                curr += timedelta(minutes=slot_length_minutes)
        return slots