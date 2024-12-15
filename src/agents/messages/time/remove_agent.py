from dataclasses import dataclass
import pykka


@dataclass(frozen=True)
class StopTimerNotificationCommand:
    actor: pykka.ActorRef


