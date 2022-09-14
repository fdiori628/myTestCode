from Components.Component.Login import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from Common.web_config_until import WebConfig


class BusinessLogin:

    def __init__(self, driver, url, username, pwd):
        self._driver = driver
        self._url = url
        self._username = username
        self._pwd = pwd

    def login(self):
        l = Login(self._driver)
        self._driver.get(self._url)
        self._driver.maximize_window()
        l.login(self._username, self._pwd)

    def getSMS(self):
        desired_cap = DesiredCapabilities.CHROME
        desired_cap["pageLoadStrategy"] = None
        driver_path = WebConfig('driver').get_appinfo()['Driver']
        driver = webdriver.Chrome(desired_capabilities=desired_cap, executable_path=driver_path)
        smsUrl = "https://smsreceivefree.com/country/usa"
        driver.get(smsUrl)


if __name__ == '__main__':
    b = BusinessLogin(1, 2, 3, 4)
    b.getSMS()
    a = input()
