from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.service_management.domain.service import ServiceEntity
from src.services.service_management.repositories.service import IServiceRepository
from src.services.service_management.repositories.sql_alchemy.extensions.to_service_dao import ToServiceDAO
from src.services.service_management.models.services import Service
from src.services.service_management.routers.extensions.service import ToServiceEntity


class SQLAlchemyServiceRepository(IServiceRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__identity_map = dict()

    async def add(self, service: ServiceEntity):
        instance: Service = service @ ToServiceDAO()
        self.__session.add(instance)
        await self.__session.commit()
        await self.__session.refresh(instance)
        self.__identity_map[instance.id] = instance
        return str(instance.public_id)

    async def delete(self, service_id):
        try:
            instance = await self.__session.get(Service, service_id)
            await self.__session.delete(instance)
            await self.__session.commit()
            await self.__session.refresh(instance)
            return True

        except Exception as e:
            return False, str(e)

    async def update(self, service: ServiceEntity):
        instance: Service = service @ ToServiceDAO()
        self.__session.refresh(instance)
        await self.__session.commit()
        await self.__session.refresh(instance)

    async def get_by_id(self, service_id):
        instance = await self.__session.get(Service, service_id)
        return instance @ ToServiceEntity()


    async def get_by_public_id(self, public_id: str):
        stmt = select(Service).where(Service.public_id == public_id)
        result = await self.__session.execute(stmt)
        instance = result.scalar_one()
        return instance @ ToServiceEntity()

    async def get_parent(self, service_id):
        stmt = select(Service).where(Service.public_id == public_id)
        result = await self.__session.execute(stmt)
        instance = result.scalar_one()
        return instance @ ToServiceEntity()

    async def get_children(self, parent_id):
        stmt = select(Service).where(Service.public_id == public_id)
        result = await self.__session.execute(stmt)
        instance = result.scalar_one()
        return instance @ ToServiceEntity()

    async def get_all(self):
        stmt = select(Service).where(Service.public_id == public_id)
        result = await self.__session.execute(stmt)
        instance = result.scalar_one()
        return instance @ ToServiceEntity()

    async def get_parents(self):
        stmt = select(Service).where(Service.public_id == public_id)
        result = await self.__session.execute(stmt)
        instance = result.scalar_one()
        return instance @ ToServiceEntity()

    def __check_not_removed(self, service_id: int):
        assert self.__identity_map.get(service_id, None) is True, f"Entity {service_id} already removed"

    @classmethod
    def service_repo(cls, session: AsyncSession) -> 'IServiceRepository':
        return cls(session)