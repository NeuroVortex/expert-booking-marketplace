from src.services.service_management.contract.service_dto import ServiceDto
from src.services.service_management.repositories.service import IServiceRepository


class ServiceHandler:
    def __init__(self, service_repository: IServiceRepository):
        self.__service_repo: IServiceRepository = service_repository

    def add_service(self, service: ServiceDto):
        return self.__service_repo.add(service)