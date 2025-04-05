from pydantic import BaseModel


class GetLocation(BaseModel):
    country_region: str
    city: str
