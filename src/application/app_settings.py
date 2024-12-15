from pathlib import Path
import json
import os


class AppSetting:
    APP_SETTINGS = None
    CREDENTIALS = None
    TEST_CREDENTIALS = None

    def __init__(self):
        self.__app_settings = {}
        self._credentials = {}
        self.__evaluate_credentials()
        self.__directory = os.path.join(Path(__file__).resolve().parent.parent, "app")
        self.__test_credentials = 'credentials-test'
        self.__file_format = '.json'
        AppSetting.APP_SETTINGS = self.__load_settings()
        # AppSetting.CREDENTIALS = self.__load_credentials()
        # AppSetting.TEST_CREDENTIALS = self.__load_test_credentials()

    def __evaluate_credentials(self):
        match str(os.getenv("MODE")).upper():
            case "PROD" | "PRODUCTION":
                self.__credential = "credentials"
                self.__app_settings = "appSettingsProd"

            case "STG" | "STAGE":
                self.__credential = "credentials-stg"
                self.__app_settings = "appSettingsStg"

            case _:
                self.__credential = "credentials-dev"
                self.__app_settings = "appSettingsDev"

    def __load_settings(self):
        app_settings_name = os.getenv('APP_SETTING_NAME', self.__app_settings)
        directory = os.path.join(self.__directory, app_settings_name + self.__file_format)
        file = open(directory, encoding="utf8")
        self.__app_settings = json.load(file)
        file.close()
        self.__read_setting()
        return self.__app_settings

    def __load_credentials(self):
        credentials_name = os.getenv('CREDENTIALS_NAME', self.__credential)
        directory = os.path.join(self.__directory, self.__credential + self.__file_format)
        file = open(directory, encoding="utf8")
        self._credentials = json.load(file)
        file.close()
        self.__read_credentials()
        return self._credentials

    def __load_test_credentials(self):
        directory = os.path.join(self.__directory, self.__test_credentials + self.__file_format)
        file = open(directory, encoding="utf8")
        self.__test_credentials = json.load(file)
        file.close()
        return self.__test_credentials

    def __read_setting(self):

        debug = os.environ.get('debug', self.__app_settings['debug'])

        time_zone = os.environ.get('TIMEZONE', self.__app_settings["appConfig"]["timezone"])

        instance_num = os.environ.get('INSTANCE_NUMBER', self.__app_settings["appConfig"]["instanceNumber"])

        self.__app_settings["debug"] = debug
        self.__app_settings["appConfig"]["timezone"] = time_zone

        self.__app_settings["appConfig"]["instanceNumber"] = instance_num

    def __read_credentials(self):

        db_conf = self._credentials["databaseConfig"]
        elastic_conf = self._credentials['loggerConfig']['elastic']
        elastic_address = os.getenv('ELASTIC_SEARCH_URL_PORT', elastic_conf['address'])
        elastic_user = os.getenv('ELASTIC_SEARCH_USER', elastic_conf["user"])
        elastic_pass = os.getenv('ELASTIC_SEARCH_PASS', elastic_conf["pass"])
        elastic_index = os.getenv('ELASTIC_SEARCH_INDEX', elastic_conf["index"])

        allowed_hosts = os.environ.get('ALLOWED_HOSTS', self._credentials["appConfig"]['allowedHosts'])
        secret_key = os.environ.get('DJANGO_SECRET_KEY', self._credentials["appConfig"]["secretKey"])
        lp_db = os.getenv('SALES_DATABASE', db_conf["sales"]["url"])

        self._credentials["databaseConfig"]["sales"]["url"] = lp_db
        self._credentials["loggerConfig"]["elastic"]["address"] = elastic_address
        self._credentials["loggerConfig"]["elastic"]["user"] = elastic_user
        self._credentials["loggerConfig"]["elastic"]["pass"] = elastic_pass
        self._credentials["loggerConfig"]["elastic"]["index"] = elastic_index
        self._credentials["appConfig"]['allowedHosts'] = allowed_hosts
        self._credentials["appConfig"]["secretKey"] = secret_key