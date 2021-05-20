import sys
sys.path.append('../myFunc/')
from baidu_Search_Element import *


def baidu_search(inputValue):
    try:
        driver = webdriver.Chrome(config['driverConfig'])
        url = config["url"]
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_css_selector('.s_ipt').send_keys(inputValue)
        baiduElement_searchBar().send_keys(inputValue)
        baiduElement_submitBtn().click()
        content = baiduElement_content().text
        assert inputValue in content
        driver.quit()
    except BaseException as e:
        raise e


baidu_search('test')