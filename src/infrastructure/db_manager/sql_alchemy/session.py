from sqlalchemy import exc
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.Infrastructure.DbManager.DatabaseManagement import AsyncDatabaseManager


class AsyncDatabaseSessionManager:
    def __init__(self):
        self.session = None
        self.factory = async_sessionmaker(AsyncDatabaseManager.ENGINE, expire_on_commit=False)

    async def __aenter__(self):
        self.session = self.factory()
        await self.session.begin()
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            if not exc_type:
                await self.session.commit()
                # await self.session.refresh(self.model)

            else:
                await self.session.rollback()

        finally:
            await self.session.close()