from kink import di

from common.Asset import IPortfolioRepository
from common.Asset.WebClient.Endpoint import AssetServiceEndpoint
from common.Execution import ITaskDataRepository
from common.Market import IMarketDataWriteRepository, IMarketDataReadRepository
from common.Market.WebClient.service_endpoint import MarketServiceEndpoint
from common.MessageBroker.IConsumer import IConsumer
from common.MessageBroker.KafkaClient.KafkaConsumer import KafkaConsumer
from common.Personage.WebClient.Endpoint import PersonageServiceEndpoint
from common.WebClient.ServiceEndpoints import IAssetServiceEndpoint, IMarketServiceEndpoint
from common.WebClient.ServiceEndpoints.IPersonageServiceEndpoin import IPersonageServiceEndpoint
from src.Application.AppSetting import AppSetting
from src.Application.Asset.PortfolioRepository import PortfolioRepository
from src.Application.Execution.TaskRepository import TaskRepository
from src.Application.Market.MarketDataRepository import MarketDataRepository
from common.Contract.Logger import ICustomLogger
from common.Logger import AdvancedLogger
from common.Personage.IPersonageDataRepository import IPersonageDataRepository
from src.Application.Personage.PersonageRepository import PersonageRepository
from src.Services.ExecutionService.repository.ITaskRepository import ITaskRepository


class Bootstrap:
    def __init__(self):
        self.__logger = AdvancedLogger()
        self.__setup_logger()
        self.__setup_repositories()
        self.__setup_consumer()

    def __setup_logger(self):
        di[ICustomLogger] = self.__logger

    def __setup_consumer(self):
        di[IConsumer] = KafkaConsumer(logger=self.__logger,
                                      kafka_urls=AppSetting.CREDENTIALS["messageBroker"]["kafka"]["urls"])

    @classmethod
    def __setup_repositories(cls):
        market_data_repo = MarketDataRepository()
        di[IMarketDataWriteRepository] = market_data_repo
        di[IMarketDataReadRepository] = market_data_repo
        di[IMarketServiceEndpoint] = MarketServiceEndpoint()
        di[IAssetServiceEndpoint] = AssetServiceEndpoint()
        di[IPersonageServiceEndpoint] = PersonageServiceEndpoint()
        di[IPersonageDataRepository] = PersonageRepository()
        di[IPortfolioRepository] = PortfolioRepository()
        di[ITaskDataRepository] = TaskRepository()