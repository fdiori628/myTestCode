from Common.web_config_until import WebConfig
from Common.dom_until import DomUntil
from selenium import webdriver
from Common.root_until import RootUntil
from Common.logger_until import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaiduHome:

    def __init__(self, _driver):
        self._log = Logger()
        self._webconfig = WebConfig('test_demo_baidu')
        self._appconfig = self._webconfig.app_config
        # {'baidu_Home': {'search': {'search_input': '.s_ipt', 'submit_btn': '.s_btn'}}}
        self._pageobj = self._webconfig.domelements['home']
        self._driver = _driver
        # findelement(d, csselector, timeout, timeseq):
        self._findele = DomUntil.findelement
        self.title = _driver.title

    def search_bar(self):
        css = self._pageobj['search_input']
        self._log.logger_debug(f'css selector path is {css}')
        ele = self._findele(self._driver, css, 5, 0.5)
        return ele

    def search_bar_input(self, message):
        ele = BaiduHome(self._driver).search_bar()
        ele.send_keys(message)
        self._log.logger_debug(f'input {message} to baidu search bar')

    def submit_btn(self):
        css = self._pageobj['submit_btn']
        self._log.logger_debug(f'css selector path is {css}')
        ele = self._findele(self._driver, css, 5, 0.5)
        return ele

    def submit_btn_click(self):
        ele = BaiduHome(self._driver).submit_btn()
        ele.click()


if __name__ == '__main__':
    path = RootUntil().get_driver
    driver = webdriver.Chrome(path)
    driver.get('http://www.baidu.com')
    b = BaiduHome(driver)
    b.search_bar_input('test')
    b.submit_btn_click()
    WebDriverWait(driver, 3, 0.5).until(EC.title_contains('test'))
    title = driver.title
    assert title == 'test_百度搜索'
    driver.quit()