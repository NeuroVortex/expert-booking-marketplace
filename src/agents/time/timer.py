import copy
import pykka
import time

from kink import inject

from src.agents.messages.time.add_agent import StartTimerNotificationCommand
from src.agents.messages.time.remove_agent import StopTimerNotificationCommand
from src.agents.messages.time.signal import TimeSignal
from src.application.time.timer import Timer
from src.shared.logger.logger_interface import ICustomLogger
from src.shared.time.mode import TimeMode


@inject
class TimerActor(pykka.ThreadingActor):
    def __init__(self, logger: ICustomLogger, timer: Timer):
        super().__init__()
        self.actorTable = {}
        self.__timer = timer
        self.__logger = logger
        self.__timer.create(self.actor_ref)
        self.__timer.postpone_call(self.actor_ref, 1, TimeMode.Periodic)
        self.time = time.time()

    def on_receive(self, msg):
        if isinstance(msg, TimeSignal):
            self.__check()

        elif isinstance(msg, StartTimerNotificationCommand):
            self.__add_actor(msg)

        elif isinstance(msg, StopTimerNotificationCommand):
            self.__remove_actor(msg.actor)

    def __check(self):
        self.time = time.time()
        actors = copy.copy(list(self.actorTable.items()))
        [self.__send_start_command(algorithmRef, startTime) for algorithmRef, startTime in actors]

    def __send_start_command(self, actor_ref: pykka.ActorRef, start_time):
        if self.time >= start_time:
            self.actorTable[actor_ref] = 2 * self.time

            try:
                actor_ref.tell(TimeSignal())

            except pykka.ActorDeadError:
                self.__delete_actor(actor_ref)

            except Exception as e:
                self.__delete_actor(actor_ref)
                self.__logger.error(str(e), e)

    def __add_actor(self, msg: StartTimerNotificationCommand):
        self.actorTable[msg.actor] = msg.start_time

    def __remove_actor(self, actor_ref: pykka.ActorRef):
        self.__delete_actor(actor_ref)

    def __delete_actor(self, actor_ref: pykka.ActorRef):
        try:
            del self.actorTable[actor_ref]

        except Exception as e:
            self.__logger.error(str(e), e)
