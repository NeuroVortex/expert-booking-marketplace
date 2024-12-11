import asyncio
import logging

from src import settings
from src.Application.AppSetting import AppSetting
from src.Infrastructure.DbManager.DatabaseManagement import AsyncDatabaseManager

logger = logging.getLogger(__name__)


class CreateDatabase:

    def __init__(self):
        self.__settings = settings
        self.__db_manager = AsyncDatabaseManager(AppSetting.CREDENTIALS["DatabaseConfig"]["marketMaking"]["URL"])

    async def run(self):
        await self.__db_manager.drop_all_tables()
        await self.__db_manager.create_all_tables(self.__settings.Registered_Models)


if __name__ == '__main__':
    asyncio.run(CreateDatabase().run())