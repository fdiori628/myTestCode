from Common.web_config_until import WebConfig
from Components.Component.VisibilityLayer.Dashboard.Dashboard import Dashboard
from Components.Component.VisibilityLayer.Dashboard.ChartEdit import ChartEdit
from Components.Component.VisibilityLayer.Dashboard.Properties.values import Values
from time import sleep
from Common.logger_until import Logger
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common
from Common.dom_until import DomUntil
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BusinessValues:

    def __init__(self, driver):
        self.driver = driver
        self.dom = DomUntil(driver)
        self.dashboard = Dashboard(driver)
        self.chartEdit = ChartEdit(driver)
        self.values = Values(driver)
        self._webconfig = WebConfig('Properties_common/values')
        self._pageobj = self._webconfig.domelements
        self.logger = Logger()
        self.common = Common(driver)

