from pydantic import BaseModel


class LocationDto(BaseModel):
    country_region: str
    city: str
