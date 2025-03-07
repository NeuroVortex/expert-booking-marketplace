from sqlalchemy.ext.asyncio import AsyncSession

from src.services.service_management.contract.service_dto import ServiceDto
from src.services.service_management.repositories.service import IServiceRepository
from src.services.service_management.repositories.sql_alchemy.extensions.to_service_dao import ToServiceDAO
from src.services.service_management.schemas.services import ServiceSchema


class SQLAlchemyServiceRepository(IServiceRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__identity_map = dict()

    async def add(self, service: ServiceDto):
        instance: ServiceSchema = service @ ToServiceDAO()
        async with self.__session as session:
            session.add(instance)
            await session.commit()
            await session.refresh(instance)

        self.__identity_map[instance.service_id] = instance
        return instance.service_id

    async def delete(self, service_id):
        pass

    async def update(self, service):
        pass

    async def get(self, service):
        pass

    async def get_by_id(self, service):
        pass

    async def get_by_identifier(self, service_identifier: str):
        pass

    async def get_parents(self):
        raise NotImplementedError

    async def get_children(self, parent_id):
        pass

    async def get_all(self):
        pass