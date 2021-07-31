from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml

testElementFile = open('../Resource/test_demo_baidu/testElement.yaml', 'r')
testElement = yaml.load(testElementFile, Loader=yaml.BaseLoader)


def myFindElement(d, cssSelector, timeout, timeSeq):
    try:
        WebDriverWait(d, timeout, timeSeq).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))
        element = d.find_element_by_css_selector(cssSelector)
    except BaseException as err:
        raise err
    return element
