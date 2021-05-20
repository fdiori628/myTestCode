from selenium import webdriver
import yaml
import pytest
import sys
sys.path.append('../myFunc/')
import myfunc_phare1

configFile = open('../Resource/test_demo_baidu/testSelenium_config.yaml', 'r')
config = yaml.load(configFile, Loader=yaml.FullLoader)

testdataFile = open('../Resource/test_demo_baidu/testSelenium_Data.yaml', 'r')
testData = yaml.load(testdataFile, Loader=yaml.FullLoader)
searchData = testData["test_search_data"]

testElementFile = open('../Resource/test_demo_baidu/testElement.yaml', 'r')
testElement = yaml.load(testElementFile, Loader=yaml.FullLoader)

findElement = myfunc_phare1.myFindElement


@pytest.mark.parametrize('inputValue', searchData)
def test_search(inputValue):
    print('testing is started')
    try:
        driver = webdriver.Chrome(config['driverConfig'])
        url = testData['test_url_homepage']
        driver.get(url)
        driver.maximize_window()
        findElement(driver, testElement["searchBar"], 3, 0.5).send_keys(inputValue)
        findElement(driver, testElement["submitBtn"], 3, 0.5).click()
        content = findElement(driver, '#' + testElement["targetContent"], 3, 0.5).text
        assert inputValue in content
        driver.quit()
    except BaseException as e:
        raise e
