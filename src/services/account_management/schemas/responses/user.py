from http.client import HTTPException

from pydantic import BaseModel


class UserAddedSuccessfully(BaseModel):
    public_id: str
    msg: str = "user added successfully"

class UserDeletedSuccessfully(BaseModel):
    msg: str = "user deleted successfully"

class UserDeletedUnSuccessfully(HTTPException):
    status_code = 500
    detail = "user deleted unsuccessfully"
