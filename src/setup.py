import asyncio
import logging
from decimal import getcontext

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from kink import inject
from starlette.middleware.cors import CORSMiddleware

from src.agents.actor_system import ActorSystem
from src.application.app_settings import AppSetting
from src.application.time.timer import Timer
from src.infrastructure.db_manager.db_checker import DBChecking
from src.services.sales.dependencies.dependencies import Dependencies
from src.settings import Registered_Models, Routers, DECIMAL_PRECISION, DECIMAL_ROUNDING, EXECUTORS, JOB_DEFAULTS, \
    Allowed_Origins, Allowed_Headers, Allow_Credentials, Allowed_Methods
from src.infrastructure.db_manager.db_management import AsyncDatabaseManager
from src.shared.logger.logger_interface import ICustomLogger


@inject
class Setup:
    db_manager: AsyncDatabaseManager | None = None
    actor_system: ActorSystem = None
    time_scheduler: AsyncIOScheduler = None
    timer: Timer = None
    loop: asyncio.AbstractEventLoop = None

    def __init__(self, logger: ICustomLogger, app: FastAPI, debug=False):
        self.app = app
        self.__logger: ICustomLogger = logger
        self.__debug = debug

    async def setup(self):
        self.__setup_logger()
        # await self.configure_db()
        await self.config_routes()
        # self.__run()

    def __setup_logger(self):
        self.__configure_logging()
        self.__logger = Dependencies.DependencyInjector.logger()

    @classmethod
    def __setup_timer(cls):
        Setup.time_scheduler = AsyncIOScheduler(executors=EXECUTORS, job_defaults=JOB_DEFAULTS)
        Setup.timer = Timer(scheduler=Setup.time_scheduler)
        Setup.time_scheduler.start()

    @classmethod
    def shutdown_timer(cls):
        Setup.timer.shutdown()

    async def configure_db(self):
        Setup.db_manager = AsyncDatabaseManager(AppSetting.CREDENTIALS["DatabaseConfig"]["marketMaking"]["URL"])

        try:
            await DBChecking().check_tables_existence(Registered_Models)

        except Exception as e:
            self.__logger.error(f"One or many table do not exist at database. Missing Table {str(e)}", )
            await self.db_manager.create_all_tables(Registered_Models)

        Setup.DbEngine = self.db_manager.ENGINE

    async def config_routes(self):
        for router in Routers:
            self.app.include_router(router.router, prefix=router.prefix, tags=router.tags)

    @classmethod
    def __configure_logging(cls):
        logging.basicConfig(
            level=logging.INFO,  # Set the desired log level
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

    @classmethod
    def __config_decimal(cls):
        getcontext().rounding = DECIMAL_ROUNDING
        getcontext().prec = DECIMAL_PRECISION

    def __setup_async_loop(self):
        Setup.loop = asyncio.get_event_loop()
        Setup.loop.set_debug(self.__debug)

    def __run(self):
        self.__setup_async_loop()
        self.__setup_timer()
        Setup.actor_system = ActorSystem(initial_actor=Manager, event_loop=Setup.loop, timer=Setup.timer)
        Setup.actor_system.start()
        Setup.consumer.start()

    @property
    def db_models(self):
        return Registered_Models