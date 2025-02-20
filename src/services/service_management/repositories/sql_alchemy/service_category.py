from sqlalchemy.ext.asyncio import AsyncSession
from src.Domain.Contract.Personage.Trader import TraderInfo
from src.Services.CopyService.models.TraderModel import TraderModel
from src.Services.CopyService.repositories.ITraderRepository import ITraderRepository
from sqlalchemy import select, and_


class SqlAlchemyCategoryRepository():
    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__identity_map = dict()

    async def add(self, trader: TraderInfo):
        instance = TraderModel.to_model(trader)
        self.__session.add(instance)
        await self.__session.commit()
        await self.__session.refresh(instance)
        trader.db_id = instance.id
        self.__identity_map[instance.id] = trader

    async def remove(self, trader: TraderInfo):
        self.__check_not_removed(trader)
        self.__identity_map[trader.db_id] = False
        trader_row = self.__session.get(TraderModel, trader.db_id)
        await self.__session.delete(trader_row)

    async def stop(self, trader: TraderInfo):
        await self.__session.get(TraderModel, trader.db_id)
        trader.is_active = False
        instance = TraderModel.to_model(trader)
        await self.__session.merge(instance)

    async def update(self, trader: TraderInfo):
        await self.__session.get(TraderModel, trader.db_id)
        instance = TraderModel.to_model(trader)
        await self.__session.merge(instance)

    async def get_by_identity(self, identity: str) -> TraderInfo:
        stmt = select(TraderModel).where(TraderModel.trader_identifier == identity)
        result = await self.__session.execute(stmt)
        trader_model: TraderModel = result.scalar_one()
        return trader_model.to_trader()

    def get_followers_by_trader_identity(self, identity: int):
        pass

    async def get_by_id(self, db_id: int) -> TraderInfo:
        instance = await self.__session.get(TraderModel, db_id)
        return self._get_entity(instance)

    async def get_actives(self) -> list[TraderInfo]:
        stmt = select(TraderModel).where(TraderModel.is_active == True)
        result = await self.__session.execute(stmt)
        traders = [trader.to_trader() for trader in result.scalars()]
        return traders

    async def is_exist(self, identity: int) -> bool:
        stmt = select(TraderModel).where(and_(TraderModel.trader_identifier == identity,
                                              TraderModel.is_active == True))
        result = await self.__session.execute(stmt)
        trader = result.scalars().first()

        if trader:
            return True

        else:
            return False

    def _get_entity(self, instance):
        if instance is None:
            return None

        entity = TraderModel.to_trader(instance)
        self.__check_not_removed(entity)

        if entity.db_id in self.__identity_map:
            return self.__identity_map[entity.db_id]

        self.__identity_map[entity.db_id] = entity
        return entity

    def __getter__(self, index):
        return self.get_by_id(index)

    def __check_not_removed(self, trader: TraderInfo):
        assert self.__identity_map.get(trader.db_id, None) is True, f"Entity {trader.db_id} already removed"

    def persist(self, trader: TraderInfo):
        self.__check_not_removed(trader)
        assert trader.db_id in self.__identity_map, ("Cannon persist entity which is unknown to the repo. "
                                                     "Did you forget to call repo.add() for this entity?")
        instance = TraderModel.to_model(trader)
        merged = self.__session.merge(instance)
        self.__session.add(merged)

    def persist_all(self):
        for entity in self.__identity_map:
            if bool(entity):
                self.persist(entity)

    @classmethod
    def trader_repo(cls, session: AsyncSession) -> 'SqlAlchemyTraderRepository':
        return cls(session=session)