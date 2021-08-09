from selenium import webdriver
from POM.Domelement.baidu_Search_Element import *
from Common.yaml_until import YamlUtil

config = YamlUtil('../Resource/test_demo_baidu/testSelenium_config.yaml').read_yaml()


def baidu_search(inputvalue):
    caps = {"pageLoadStrategy": "eager"}
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        # driver = webdriver.Chrome(desired_capabilities=caps, executable_path=config['driverConfig'])
        driver = webdriver.Chrome(desired_capabilities=caps, executable_path=config['driverConfig'],
                                  options=chrome_options)
        url = config["url"]
        driver.get(url)
        driver.maximize_window()
        baiduelement_searchbar(driver).send_keys(inputvalue)
        baiduelement_submitbtn(driver).click()
        content = baiduelement_content(driver).text
        driver.quit()
        return content
    except BaseException as e:
        raise e
