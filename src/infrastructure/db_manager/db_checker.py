from sqlalchemy import inspect

from src.Infrastructure.DbManager.DatabaseManagement import AsyncDatabaseManager
from src.Infrastructure.DbManager.Exception.DatabaseDoesNotExist import DatabaseDoesNotExist


class DBChecking:

    async def check_tables_existence(self, db_models: list):
        db_names = [table.__tablename__ for table in db_models]

        async with AsyncDatabaseManager.ENGINE.connect() as conn:
            result = await conn.run_sync(self._inspect_tables)

            missing_tables = [
                table for table in db_names
                if table not in result]

            if missing_tables:
                raise DatabaseDoesNotExist

    @classmethod
    def _inspect_tables(cls, conn):
        """Synchronous code to inspect tables, to be run in an async context."""
        inspector = inspect(conn)
        tables_in_db = inspector.get_table_names()
        return tables_in_db