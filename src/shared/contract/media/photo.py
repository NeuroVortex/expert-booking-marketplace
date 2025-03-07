from datetime import datetime
from typing import NamedTuple


class Photo(NamedTuple):
    file_url: str
    file_name: str
    size: int
    content_type: str
    created_at: datetime


