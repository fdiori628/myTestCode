import sys
import yaml

sys.path.append('../myFunc/')
import myfunc_phare1
from selenium import webdriver

configFile = open('../Resource/test_demo_baidu/testSelenium_config.yaml', 'r')
config = yaml.load(configFile, Loader=yaml.FullLoader)

testElementFile = open('../Resource/test_demo_baidu/testElement.yaml', 'r')
testElement = yaml.load(testElementFile, Loader=yaml.FullLoader)

driver = webdriver.Chrome(config['driverConfig'])

findElement = myfunc_phare1.myFindElement


def baiduElement_searchBar():
    e = findElement(driver, testElement["searchBar"], 3, 0.5)
    return e


def baiduElement_submitBtn():
    e = findElement(driver, testElement["submitBtn"], 3, 0.5)
    return e


def baiduElement_content():
    e = findElement(driver, '#' + testElement["targetContent"], 3, 0.5)
    return e
