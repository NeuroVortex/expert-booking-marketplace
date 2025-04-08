from pydantic import BaseModel

from src.schema.location import GetLocation


class GetProfile(BaseModel):
    name: str
    location: GetLocation