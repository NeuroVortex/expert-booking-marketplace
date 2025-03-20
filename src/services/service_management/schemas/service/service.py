from pydantic import BaseModel, Field


class ServiceDto(BaseModel):
    name: str
    description: str
    parent_public_id: str | None = Field(None)
