from pydantic import BaseModel


class ServiceModel(BaseModel):
    Name: str
    Description: str
    Hover: str

