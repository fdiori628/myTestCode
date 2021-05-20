from selenium import webdriver
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MYFUNCSELENIUM():

    def __init__(self):
        self.configFile = open('../Resource/test_demo_baidu/testSelenium_config.yaml', 'r')
        self.config = yaml.load(self.configFile, Loader=None)
        self.driver = webdriver.Chrome(self.config['driverConfig'])
        self.dataFile = open('../Resource/test_demo_baidu/testSelenium_Data.yaml', 'r')
        self.testData = yaml.load(self.dataFile, Loader=None)
        self.url_pharse1 = self.testData['test_url_pharse1']

    def demo_test_name(self):
        self.driver.get(self.url_pharse1)
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.s_ipt')))
        self.driver.find_element_by_css_selector('.s_ipt')


if __name__ == '__main__':
    m = MYFUNCSELENIUM()
    m.demo_test_name()
