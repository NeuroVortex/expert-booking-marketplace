from pydantic import BaseModel


class UserAddressDto(BaseModel):
    title: str
    user_public_id: str
    province: str
    city: str
    homeNumber: str
    firstLineAddress: str
    secondLineAddress: str | None
    zipCode: str
