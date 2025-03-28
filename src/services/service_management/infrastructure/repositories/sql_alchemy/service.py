from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.service_management.domain.entities.service import ServiceEntity

from src.services.service_management.infrastructure.repositories.extensions.to_service import ModelToServiceEntity, \
    EntityToServiceModel
from src.services.service_management.infrastructure.repositories.extensions.to_updated_service import ToUpdatedService
from src.services.service_management.infrastructure.repositories.service import IServiceRepository
from src.services.service_management.infrastructure.models.services import Service


class SQLAlchemyServiceRepository(IServiceRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__identity_map = dict()

    async def add(self, service: ServiceEntity):
        instance: Service = service @ EntityToServiceModel()
        self.__session.add(instance)
        await self.__session.commit()
        await self.__session.refresh(instance)
        self.__identity_map[instance.id] = instance
        return str(instance.public_id)

    async def delete(self, service_id):
        stmt = select(Service).where(Service.public_id == service_id)
        result = await self.__session.execute(stmt)
        instance = result.scalar_one()
        await self.__session.delete(instance)

    async def update(self, service: ServiceEntity):
        updated_instance: dict = service @ ToUpdatedService()
        instance = await self.__session.get(Service, service.id)

        for key, value in updated_instance.items():
            setattr(instance, key, value)

        await self.__session.commit()
        await self.__session.refresh(instance)

    async def get_by_id(self, service_id):
        instance = await self.__session.get(Service, service_id)
        return instance @ ModelToServiceEntity()


    async def get_by_public_id(self, public_id: str):
        stmt = select(Service).where(Service.public_id == public_id)
        result = await self.__session.execute(stmt)
        instance = result.scalar_one()
        return instance @ ModelToServiceEntity()

    async def get_services(self, parent_public_id: str | None = None):
        if parent_public_id is None:
            stmt = select(Service).where(Service.parent_service_id.is_(None))

        else:
            parent_id_subquery = select(Service.id).where(Service.public_id == parent_public_id).scalar_subquery()
            stmt = select(Service).where(Service.parent_service_id == parent_id_subquery)

        result = await self.__session.execute(stmt)
        instances = result.scalars()
        services = [instance @ ModelToServiceEntity() for instance in instances]
        return services

    async def get_bulk_services(self, parent_public_ids: list[str]):
        stmt = select(Service).where(Service.public_id.in_(parent_public_ids))
        result = await self.__session.execute(stmt)
        services = [instance @ ModelToServiceEntity() for instance in result.scalars()]
        return services

    async def get_all(self) -> list[ServiceEntity]:
        stmt = select(Service)
        result = await self.__session.execute(stmt)
        instances = result.scalars()
        services = [instance @ ModelToServiceEntity() for instance in instances]
        return services

    def __check_not_removed(self, service_id: int):
        assert self.__identity_map.get(service_id, None) is True, f"Entity {service_id} already removed"

    @classmethod
    def service_repo(cls, session: AsyncSession) -> 'IServiceRepository':
        return cls(session)