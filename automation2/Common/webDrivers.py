from selenium import webdriver
from Common.web_config_until import WebConfig


class WebDrivers:

    def __init__(self):
        self.driver_path = WebConfig('driver').get_appinfo()['Driver']

    def driver(self):
        d = webdriver.Chrome(self.driver_path)
        return d

    def driver_headless(self):
        caps = {"pageLoadStrategy": "eager"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        d = webdriver.Chrome(desired_capabilities=caps, executable_path=self.driver_path, options=chrome_options)
        return d
