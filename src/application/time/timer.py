from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.job import Job
from datetime import datetime
from kink import inject
import pykka
import pytz

from src.agents.messages.time.signal import TimeSignal
from src.app.app_settings import AppSettings
from src.shared.logger.logger_interface import ICustomLogger
from src.shared.time.mode import TimeMode


@inject
class Timer:
    def __init__(self, logger: ICustomLogger, scheduler: AsyncIOScheduler):
        super().__init__()
        self.__scheduler = scheduler
        self.__time_zone = AppSettings.APP_SETTINGS['appConfig']['timezone']
        self.__identityRepository: dict[pykka.ActorRef, str] = {}
        self.__lastTriggered: dict[pykka.ActorRef, datetime] = {}
        self.__jobs: dict[pykka.ActorRef, Job] = {}
        mode = AppSettings.APP_SETTINGS['appConfig']['timeMode']
        self.__time_mode = TimeMode[str(mode).capitalize()]
        self.__logger = logger

    def create(self, actor: pykka.ActorRef):
        self.__identityRepository[actor] = str(actor)
        self.__lastTriggered[actor] = datetime.now(tz=pytz.timezone(self.__time_zone))

    def __delete(self, actor: pykka.ActorRef):
        if actor in self.__identityRepository:
            del self.__identityRepository[actor]

        if actor in self.__jobs:
            del self.__jobs[actor]

        if actor in self.__lastTriggered:
            del self.__lastTriggered[actor]

    def stop(self, actor: pykka.ActorRef):

        if actor in self.__jobs:
            self.__jobs[actor].remove()
        self.__delete(actor)

    def shutdown(self):
        self.__scheduler.shutdown(wait=False)

    def postpone_call(self, actor: pykka.ActorRef, duration: float, call_type: TimeMode = TimeMode.Periodic):

        match call_type:
            case TimeMode.Static:
                self.__statical_interval_postpone_call(actor, int(duration))

            case TimeMode.Dynamic:
                self.__dynamical_interval_postpone_call(actor, int(duration))

            case TimeMode.Periodic:
                self.__periodic_call(actor, int(duration))

    def immediate_call(self, actor: pykka.ActorRef):
        self.__jobs[actor] = self.__scheduler.add_job(self.__call,
                                                      args=[actor],
                                                      id=self.__identityRepository[actor],
                                                      timezone=pytz.timezone(self.__time_zone),
                                                      replace_existing=True)

    def __periodic_call(self, actor: pykka.ActorRef, duration: int):
        now = datetime.now(tz=pytz.timezone(self.__time_zone))
        self.__jobs[actor] = self.__scheduler.add_job(self.__call,
                                                      'interval',
                                                      args=[actor, TimeMode.Periodic],
                                                      seconds=duration,
                                                      start_date=now,
                                                      id=self.__identityRepository[actor],
                                                      timezone=pytz.timezone(self.__time_zone),
                                                      replace_existing=True)

    def __statical_interval_postpone_call(self, actor: pykka.ActorRef, duration: int):
        now = datetime.now(tz=pytz.timezone(self.__time_zone))
        self.__jobs[actor] = self.__scheduler.add_job(self.__call,
                                                      'interval',
                                                      args=[actor, TimeMode.Static],
                                                      seconds=duration,
                                                      start_date=now,
                                                      id=self.__identityRepository[actor],
                                                      timezone=pytz.timezone(self.__time_zone),
                                                      replace_existing=True)

    def __dynamical_interval_postpone_call(self, actor: pykka.ActorRef, duration: float):
        self.__jobs[actor] = self.__scheduler.add_job(self.__call,
                                                      'interval',
                                                      args=[actor, TimeMode.Dynamic],
                                                      seconds=duration,
                                                      start_date=self.__lastTriggered[actor],
                                                      id=self.__identityRepository[actor],
                                                      timezone=pytz.timezone(self.__time_zone),
                                                      replace_existing=True)

    def __call(self, actor_ref: pykka.ActorRef, call_type: TimeMode):
        try:

            match call_type:
                case TimeMode.Static:
                    self.__jobs[actor_ref].remove()
                    actor_ref.tell(TimeSignal())

                case TimeMode.Dynamic:
                    self.__jobs[actor_ref].remove()
                    actor_ref.tell(TimeSignal())

                case TimeMode.Periodic:
                    actor_ref.tell(TimeSignal())

        except Exception as e:
            self.stop(actor_ref)
            self.__delete(actor_ref)
            self.__logger.error('Error has been occurred while send TimeSignal Message', 'Timer', e)