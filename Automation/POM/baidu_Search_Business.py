import sys
from selenium import webdriver
sys.path.append('../myFunc/')
from baidu_Search_Element import *


def baidu_search(inputValue):
    caps = {"pageLoadStrategy": "eager"}
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        # driver = webdriver.Chrome(desired_capabilities=caps, executable_path=config['driverConfig'])
        driver = webdriver.Chrome(desired_capabilities=caps, executable_path=config['driverConfig'],
                                  chrome_options=chrome_options)
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
