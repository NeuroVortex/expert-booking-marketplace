from pydantic import BaseModel


class Client(BaseModel):
    name: str
    family_name: str
    email: str
    phone: str
    address: str
    zip_code: str
    national_code: str
