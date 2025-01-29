import asyncio


import pykka

from src.agents.messages.system.start_command import StartSystemCommand
from src.agents.time.timer import TimerActor
from src.application.time.timer import Timer


class ActorSystem:
    actor_ref: pykka.ActorRef = None
    timer_actor_ref: pykka.ActorRef = None
    event_loop: asyncio.AbstractEventLoop = None

    def __init__(self, initial_actor: pykka.ThreadingActor,
                 event_loop: asyncio.AbstractEventLoop,
                 timer: Timer = None):
        self.__actor = initial_actor
        self.__setup_loop(event_loop)
        self.__timer = timer

    def start(self):
        ActorSystem.actor_ref = self.__actor.start()
        ActorSystem.actor_ref.tell(StartSystemCommand())
        self.__setup_timer()

    @classmethod
    def __setup_loop(cls, loop: asyncio.AbstractEventLoop):
        ActorSystem.event_loop = loop

    def __setup_timer(self):
        ActorSystem.timer_actor_ref = TimerActor.start(timer=self.__timer)