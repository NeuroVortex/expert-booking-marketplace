class UserExistException(Exception):
    def __init__(self):
        super(UserExistException, self).__init__("user already exists")