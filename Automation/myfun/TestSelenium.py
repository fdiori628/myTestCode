import sys
import yaml
from selenium import webdriver
import pytest
from baidu_Search_Element import *


class TestCase:

    @pytest.mark.parametrize('inputvalue', ['react', 'github'])
    def testdemo(self, inputvalue):
        caps = {"pageLoadStrategy": "eager"}
        dataFile = open('../Resource/test_demo_baidu/testSelenium_Data.yaml', 'r')
        testData = yaml.load(dataFile, Loader=yaml.BaseLoader)
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        # driver = webdriver.Chrome(desired_capabilities=caps, executable_path='../Drivers/chromedriver.exe',
        #                           options=chrome_options)
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome('../Drivers/chromedriver.exe', options=options)
        # driver.get('http://www.taobao.com')
        driver.get('http://www.baidu.com')
        driver.quit()
        # baiduElement_searchBar(driver).send_keys(inputvalue)
        # baiduElement_submitBtn(driver).click()
        # # content = baiduElement_content(driver).text
        # content = ['react', 'github']
        #
        # assert inputvalue in content
