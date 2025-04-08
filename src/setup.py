import asyncio
import logging
from decimal import getcontext

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from kink import inject

from src.app.app_settings import AppSettings
from src.application.logger.logger_interface import ICustomLogger
from src.infrastructure.db_manager.db_checker import DBChecking
from src.application.dependencies.dependencies import Dependencies
from src.settings import Registered_Models, Routers, DECIMAL_PRECISION, DECIMAL_ROUNDING, EXECUTORS, JOB_DEFAULTS
from src.infrastructure.db_manager.db_management import AsyncDatabaseManager


@inject
class Setup:
    db_manager: AsyncDatabaseManager | None = None
    time_scheduler: AsyncIOScheduler = None
    loop: asyncio.AbstractEventLoop = None

    def __init__(self, logger: ICustomLogger, app: FastAPI, debug=False):
        self.app = app
        self.__logger: ICustomLogger = logger
        self.__debug = debug

    async def setup(self):
        self.__setup_logger()
        await self.configure_db()
        await self.config_routes()
        # self.__run()

    def __setup_logger(self):
        self.__configure_logging()
        self.__logger = Dependencies.DependencyInjector.logger()

    async def configure_db(self):
        Setup.db_manager = AsyncDatabaseManager(AppSettings.CREDENTIALS["databases"]["main"]["connection"])

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

    @property
    def db_models(self):
        return Registered_Models