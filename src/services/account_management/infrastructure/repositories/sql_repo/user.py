from sqlalchemy import select, exists
from sqlalchemy.sql import or_
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.exceptions.db_exceptions import DoesNotExist
from src.services.account_management.infrastructure.repositories.extensions.user_model import ToUserModel, ToUser
from src.services.account_management.infrastructure.models.user import User
from src.services.account_management.infrastructure.repositories.user import IUserRepository
from src.shared.account.user import UserEntity


class SqlAlchemyUserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__identity_map = dict()

    async def create(self, user: UserEntity) -> str:
        instance = user @ ToUserModel()
        self.__session.add(instance)
        await self.__session.commit()
        await self.__session.refresh(instance)
        self.__identity_map[instance.public_id] = instance
        return str(instance.public_id)

    async def remove(self, user_public_id: str):
        try:
            stmt = select(User).where(User.public_id == user_public_id)
            result = await self.__session.execute(stmt)
            instance = result.scalar_one()
            await self.__session.delete(instance)

        except NoResultFound:
            raise DoesNotExist()

    async def get_by_user_public_id(self, public_id: str) -> UserEntity:
        try:
            stmt = select(User).where(User.public_id == public_id)
            result = await self.__session.execute(stmt)
            instance: User = result.scalar_one()
            return instance @ ToUser()

        except NoResultFound:
            raise DoesNotExist()

    async def get_by_phone(self, phone: str) -> UserEntity:
        stmt = select(User).where(User.primary_phone == phone)
        result = await self.__session.execute(stmt)
        instance: User = result.scalar_one()
        return instance @ ToUser()

    async def get_by_email(self, email: str) -> UserEntity:
        stmt = select(User).where(User.primary_email == email)
        result = await self.__session.execute(stmt)
        instance: User = result.scalar_one()
        return instance @ ToUser()

    async def get_by_identification(self, identification: str) -> UserEntity:
        stmt = select(User).where(User.identifier == identification)
        result = await self.__session.execute(stmt)
        instance: User = result.scalar_one()
        return instance @ ToUser()

    async def update(self, user):
        instance = user @ ToUserModel
        self.__session.add(instance)
        await self.__session.commit()
        await self.__session.refresh(instance)
        update_user = instance @ ToUser()
        self.__identity_map[instance.user_id] = instance
        return update_user

    async def is_exist(self, user: UserEntity):
        stmt = select(exists().where(or_(User.primary_email == user.email,
                                      User.primary_phone == user.phone)))

        instance = await self.__session.execute(stmt)
        return instance.scalar()

    @classmethod
    def user_repo(cls, session: AsyncSession):
        return cls(session)