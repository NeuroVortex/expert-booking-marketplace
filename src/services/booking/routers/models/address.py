from pydantic import BaseModel


class Address(BaseModel):
    province: str
    city: str
    homeNumber: str
    firstLineAddress: str
    secondLineAddress: str | None
    zipCode: str
