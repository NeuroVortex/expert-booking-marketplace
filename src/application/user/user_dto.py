class ToUser:
    def __rmatmul__(self, other):
        return other

class ToModel:
    def __rmatmul__(self, other):
        return other
