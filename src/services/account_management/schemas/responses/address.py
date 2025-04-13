from pydantic import BaseModel


class GetAddress(BaseModel):
    public_id: str
    user_public_id: str
    province: str
    city: str
    homeNumber: str
    firstLineAddress: str
    secondLineAddress: str | None
    zipCode: str