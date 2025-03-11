from src.services.service_management.handlers.service import ServiceHandler
from kink import di

from src.services.service_management.repositories.service import IServiceRepository
from src.services.service_management.repositories.sql_alchemy.service import SQLAlchemyServiceRepository


class Dependencies:
    Dependency = None

    def __init__(self):
        di[IServiceRepository] = SQLAlchemyServiceRepository
        Dependencies.Dependency = self

    @classmethod
    def service_handler(cls) -> ServiceHandler:
        return ServiceHandler()
