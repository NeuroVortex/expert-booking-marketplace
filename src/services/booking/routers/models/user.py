from pydantic import BaseModel


class UserModel(BaseModel):
    firstName: str
    lastName: str
    email: str
    phone: str
    identityNumber: str
