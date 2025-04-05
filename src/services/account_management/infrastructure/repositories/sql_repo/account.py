from src.services.account_management.infrastructure.repositories.account import IAccountRepository


class AccountRepository(IAccountRepository):
    def create(self, account):
        pass

    def get(self, account):
        pass

    def get_by_user(self, user):
        pass

    def get_by_user_and_platform(self, user, platform):
        pass

    def update(self, account):
        pass