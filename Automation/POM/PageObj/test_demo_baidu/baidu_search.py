from Common.web_config_until import WebConfig
from Common.dom_until import DomUntil
from selenium import webdriver
from Common.root_until import RootUntil
from Common.logger_until import Logger
from POM.PageObj.test_demo_baidu.baidu_Home import BaiduHome


class BaiduSearch:

    def __init__(self, _driver):
        self.title = _driver.title
        self._log = Logger()
        self._webconfig = WebConfig('test_demo_baidu')
        self._appconfig = self._webconfig.app_config
        # 'search': {'content_left': '#content_left'}}
        self._pageobj = self._webconfig.domelements['search']
        self._driver = _driver
        # findelement(d, csselector, timeout, timeseq):
        self._findele = DomUntil.findelement

    def content_left_firstele(self):
        css = self._pageobj['content_left']
        ele = self._findele(self._driver, css, 5, 0.5)
        return ele


if __name__ == '__main__':
    driver = WebConfig('test').get_driver
    driver.get('http://www.baidu.com')
    b = BaiduSearch(driver)
    bh = BaiduHome(driver)
    bh.search_bar_input('test')
    bh.submit_btn_click()
    _ele = b.content_left_firstele()
    assert 'test - 百度翻译' in _ele.text
    driver.quit()
