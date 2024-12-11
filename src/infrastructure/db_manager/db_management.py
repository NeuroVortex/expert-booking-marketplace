from contextlib import contextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, joinedload, DeclarativeBase
from sqlalchemy import exc


class AsyncDatabaseManager:
    ENGINE: AsyncEngine | None = None
    Base: DeclarativeBase | None = declarative_base()
    SessionFactory: async_sessionmaker[AsyncSession] | None = sessionmaker

    def __init__(self, db_url):
        AsyncDatabaseManager.ENGINE = create_async_engine(db_url, echo=False)
        AsyncDatabaseManager.Base = declarative_base()
        AsyncDatabaseManager.SessionFactory = sessionmaker

    @classmethod
    async def create_all_tables(cls, db_models: list):
        async with AsyncDatabaseManager.ENGINE.begin() as conn:
            for db_model in db_models:
                await conn.run_sync(db_model.metadata.create_all)

    @classmethod
    async def drop_all_tables(cls):
        async with AsyncDatabaseManager.ENGINE.begin() as conn:
            await conn.run_sync(AsyncDatabaseManager.Base.metadata.drop_all)

    @classmethod
    async def get_db_session(cls) -> AsyncGenerator[AsyncSession, None]:
        factory = async_sessionmaker(AsyncDatabaseManager.ENGINE)
        async with factory() as session:
            try:
                yield session
                await session.commit()
            except exc.SQLAlchemyError as error:
                await session.rollback()
                raise

            finally:
                await session.close()