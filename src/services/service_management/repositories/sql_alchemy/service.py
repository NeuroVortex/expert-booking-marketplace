from sqlalchemy.ext.asyncio import AsyncSession

from src.services.service_management.contract.service_dto import ServiceDto
from src.services.service_management.repositories.service import IServiceRepository
from src.services.service_management.repositories.sql_alchemy.extensions.to_service_dao import ToServiceDAO
from src.services.service_management.models.services import Service


class SQLAlchemyServiceRepository(IServiceRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__identity_map = dict()

    async def add(self, service: ServiceDto):
        instance: Service = service @ ToServiceDAO()
        async with self.__session as session:
            session.add(instance)
            await session.commit()
            await session.refresh(instance)

        self.__identity_map[instance.service_id] = instance
        return str(instance.service_public_id)

    async def delete(self, service_id):
        pass

    async def update(self, service):
        pass

    async def get_by_id(self, service_id):
        pass

    async def get_by_public_id(self, public_id: str):
        pass

    async def get_parent(self, service_id):
        pass

    async def get_children(self, parent_id):
        pass

    async def get_all(self):
        pass

    async def get_parents(self):
        pass

    @classmethod
    def service_repo(cls, session: AsyncSession) -> 'IServiceRepository':
        return cls(session)