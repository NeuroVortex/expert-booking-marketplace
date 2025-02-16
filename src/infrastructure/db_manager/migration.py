import asyncio
import logging

from src import settings
from src.app.app_settings import AppSettings
from src.infrastructure.db_manager.db_management import AsyncDatabaseManager

logger = logging.getLogger(__name__)


class CreateDatabase:

    def __init__(self):
        self.__settings = settings
        self.__db_manager = AsyncDatabaseManager(AppSettings.CREDENTIALS["databases"]["main"]["connection"])

    async def run(self):
        await self.__db_manager.drop_all_tables()
        await self.__db_manager.create_all_tables(self.__settings.Registered_Models)


if __name__ == '__main__':
    AppSettings()
    asyncio.run(CreateDatabase().run())