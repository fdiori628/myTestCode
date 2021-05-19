from selenium import webdriver
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from myFunc.myFunc_phare1 import webWait

configFile = open('../Resource/test_demo_baidu/testSelenium_config.yaml', 'r')
config = yaml.load(configFile, Loader=yaml.FullLoader)

testdataFile = open('../Resource/test_demo_baidu/testSelenium_Data.yaml', 'r')
testData = yaml.load(testdataFile, Loader=yaml.FullLoader)
searchData = testData["test_search_data"]

testElementFile = open('../Resource/test_demo_baidu/testElement.yaml', 'r')
testElement = yaml.load(testElementFile, Loader=yaml.FullLoader)


@pytest.mark.parametrize('inputValue', searchData)
def test_search(inputValue):
    print('testing is started')
    try:
        driver = webdriver.Chrome(config['driverConfig'])
        url = testData['test_url_homepage']
        driver.get(url)
        webWait(driver, 3, 0.5, testElement["searchBar"])
        driver.find_element_by_css_selector(testElement["searchBar"]).send_keys(inputValue)
        driver.find_element_by_css_selector(testElement["submitBtn"]).click()
        WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, testElement["targetContent"])))
        content = driver.find_element_by_id(testElement["targetContent"]).text
        assert inputValue in content
        driver.quit()
    except BaseException as e:
        raise e
