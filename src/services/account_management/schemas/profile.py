from pydantic import BaseModel

from src.services.account_management.schemas.location import LocationDto


class ProfileDto(BaseModel):
    name: str
    location: LocationDto
