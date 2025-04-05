from pydantic import BaseModel

from src.services.account_management.schemas.responses.location import GetLocation


class GetProfile(BaseModel):
    name: str
    location: GetLocation