from pydantic import BaseModel

from src.schema.profile import GetProfile


class GetUser(BaseModel):
    public_id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    identifier: str
    gender: str | None
    profile: GetProfile