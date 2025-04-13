class TimeSlotConflictException(Exception):
    def __init__(self):
        super(TimeSlotConflictException, self).__init__('TimeSlot Conflict')