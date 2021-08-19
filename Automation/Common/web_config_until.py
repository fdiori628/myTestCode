from Common.yaml_until import YamlUtil
from string import Template
from Common.root_until import RootUntil
from Common.logger_until import Logger
from selenium import webdriver


class WebConfig:

    def __init__(self, app_name):
        self._app_name = app_name
        self._root = RootUntil()
        self._appconfig = self._root.get_configfile[1]['WEB']
        self._rootpath = self._root.get_rootpath
        self._log = Logger()
        self._config = self._root.get_configfile

    def get_appinfo(self):
        try:
            info_list = list(self._appconfig.keys())
            tempdict = {}
            for i in info_list:
                temp = Template(self._appconfig[i])
                appname = {
                    "appname": self._app_name,
                    "rootpath": self._rootpath
                }
                result = temp.substitute(appname)
                tempdict[i] = result
            self._log.logger_debug(f'The config info is {tempdict}')
            return tempdict
        except Exception as e:
            raise e and self._log.logger_error(e)

    @property
    def report_cmd(self):
        path = WebConfig(self._app_name).get_appinfo()
        return path['ReportPath']

    @property
    def app_config(self):
        path = WebConfig(self._app_name).get_appinfo()['ConfigPath']
        config = YamlUtil(path).read_yaml()
        return config

    @property
    def testdata(self):
        path = WebConfig(self._app_name).get_appinfo()['TestDataPath']
        data = YamlUtil(path).read_yaml()
        return data

    @property
    def domelements(self):
        path = WebConfig(self._app_name).get_appinfo()['DomElement']
        elements = YamlUtil(path).read_yaml()
        return elements

    @property
    def pom_business_path(self):
        path = WebConfig(self._app_name).get_appinfo()['POM_business_path']
        return path

    # @property
    # def get_driver(self):
    #     path = WebConfig(self._app_name).get_appinfo()['Driver']
    #     _driver = webdriver.Chrome(path)
    #     self._log.logger_debug('Chrome driver is mounting')
    #     return _driver
    #
    # @property
    # def get_driver_m1(self):
    #     path = WebConfig(self._app_name).get_appinfo()['Driver-m1']
    #     _driver = webdriver.Chrome(path)
    #     self._log.logger_debug('Chrome-m1 driver is mounting')
    #     return _driver
    #
    # @property
    # def get_driver_headless(self):
    #     path = WebConfig(self._app_name).get_appinfo()['Driver']
    #     caps = {"pageLoadStrategy": "eager"}
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument("--headless")
    #     _driver = webdriver.Chrome(desired_capabilities=caps, executable_path=path, options=chrome_options)
    #     self._log.logger_debug('Chrome driver is mounting')
    #     return _driver



if __name__ == '__main__':
    w = WebConfig('test_demo_baidu')
    print(w.testdata)

