from datetime import datetime
from typing import NamedTuple


class Certificate(NamedTuple):
    name: str
    issued_organization: str
    issue_date: datetime
    expiration_date: datetime | None
    credential_id: str
    credential_url: str
