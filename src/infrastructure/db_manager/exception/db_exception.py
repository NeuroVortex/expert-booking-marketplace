class DatabaseDoesNotExist(Exception):
    def __init__(self):
        super().__init__('Database DoesNot Exist')