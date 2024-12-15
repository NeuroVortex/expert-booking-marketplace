from pydantic import BaseModel, Field, ConfigDict


class ServiceModel(BaseModel):
    Title: str
    Duration: int
    Description: str
    Price: str
