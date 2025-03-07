from src.services.service_management.handlers.service import ServiceHandler


class Dependencies:

    @classmethod
    def service_handler(cls) -> ServiceHandler:
        return ServiceHandler()
