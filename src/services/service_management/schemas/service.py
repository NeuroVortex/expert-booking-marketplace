from pydantic import BaseModel


class ServiceDetail(BaseModel):
    photo: str
    hover: str
    description: str
