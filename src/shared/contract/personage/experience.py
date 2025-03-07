from datetime import datetime
from typing import NamedTuple

from src.shared.contract.personage.employement_type import EmployeeType
from src.shared.contract.personage.location import Location


class Experience(NamedTuple):
    title: str
    employment_type: EmployeeType
    organization: str
    currently_active: bool
    start_date: datetime
    end_date: datetime
    location: Location
    description: str


