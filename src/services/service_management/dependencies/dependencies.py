
from kink import di

from src.services.service_management.application.handlers.service import ServiceHandler
from src.services.service_management.infrastructure.repositories.service import IServiceRepository
from src.services.service_management.infrastructure.repositories.sql_alchemy.service import SQLAlchemyServiceRepository


class Dependencies:
    Dependency = None

    def __init__(self):
        di[IServiceRepository] = SQLAlchemyServiceRepository
        Dependencies.Dependency = self

    @classmethod
    def service_handler(cls) -> ServiceHandler:
        return ServiceHandler()
