from pydantic import BaseModel, EmailStr

from src.services.account_management.schemas.profile import ProfileDto


class UserDto(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    identifier: str
    gender: str | None
    profile: ProfileDto
