class DoesNotExist(Exception):
    def __init__(self):
        super().__init__('There is not any result')