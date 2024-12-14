from typing import NamedTuple


class AgentBrokenMessage(NamedTuple):
    identifier: str
    exception: str