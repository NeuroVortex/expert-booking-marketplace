from dataclasses import dataclass
import pykka


@dataclass(frozen=True)
class StartTimerNotificationCommand:
    actor: pykka.ActorRef
    start_time: float