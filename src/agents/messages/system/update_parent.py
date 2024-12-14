from typing import NamedTuple
from pykka import ActorRef


class UpdateParentRef(NamedTuple):
    actor_ref: ActorRef