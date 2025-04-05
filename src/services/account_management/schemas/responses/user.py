from http.client import HTTPException

from pydantic import BaseModel

from src.services.account_management.schemas.responses.profile import GetProfile


class UserAddedSuccessfully(BaseModel):
    public_id: str
    msg: str = "user added successfully"

class UserDeletedSuccessfully(BaseModel):
    msg: str = "user deleted successfully"

class UserDeletedUnSuccessfully(HTTPException):
    status_code = 500
    detail = "user deleted unsuccessfully"

class GetUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    identifier: str
    gender: str | None
    profile: GetProfile