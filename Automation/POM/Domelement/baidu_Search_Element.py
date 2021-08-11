from Common.dom_until import DomUntil
from Common.yaml_until import YamlUtil

testElement = YamlUtil('../Resource/test_demo_baidu/testElement.yaml').read_yaml()
findelement = DomUntil.findelement


def baiduelement_searchbar(driver):
    e = findelement(driver, testElement["searchBar"], 3, 0.5)
    return e


def baiduelement_submitbtn(driver):
    e = findelement(driver, testElement["submitBtn"], 3, 0.5)
    return e


def baiduelement_content(driver):
    e = findelement(driver, '#' + testElement["targetContent"], 3, 0.5)
    return e
