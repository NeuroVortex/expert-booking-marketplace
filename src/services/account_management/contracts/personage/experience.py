from datetime import datetime
from typing import NamedTuple

from src.services.account_management.contracts.personage.employement_type import EmployeeType
from src.services.account_management.contracts.personage.location import Location


class Experience(NamedTuple):
    title: str
    employment_type: EmployeeType
    organization: str
    currently_active: bool
    start_date: datetime
    end_date: datetime
    location: Location
    description: str


