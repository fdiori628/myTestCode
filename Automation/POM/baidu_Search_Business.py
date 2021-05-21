import sys
from selenium import webdriver
sys.path.append('../myFunc/')
from baidu_Search_Element import *


def baidu_search(inputValue):
    try:
        driver = webdriver.Chrome(config['driverConfig'])
        url = config["url"]
        driver.get(url)
        driver.maximize_window()
        baiduElement_searchBar(driver).send_keys(inputValue)
        baiduElement_submitBtn(driver).click()
        content = baiduElement_content(driver).text
        assert inputValue in content
        driver.quit()
    except BaseException as e:
        raise e
