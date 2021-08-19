from POM.PageObj.test_demo_baidu.baidu_Home import BaiduHome
from POM.PageObj.test_demo_baidu.baidu_search import BaiduSearch
from Common.web_config_until import WebConfig
from Common.logger_until import Logger

class BaiduSearchBusiness:

    def __init__(self, driver):
        self._log = Logger()
        self._home = BaiduHome(driver)
        self._search = BaiduSearch(driver)
        self._driver = driver
        self._url = WebConfig('test_demo_baidu').app_config['domain_url']

    def baidu_searching(self, context):
        self._driver.get(self._url)
        self._log.logger(f'visiting {self._url}')
        self._home.search_bar_input(context)
        self._log.logger(f'inputing {context} to search bar')
        self._home.submit_btn_click()
        self._log.logger(f'Clicking submit btn')
        result = self._search.content_left_firstele()
        log_result = result.text
        self._log.logger(f'got the result as {log_result}')
        return result


if __name__ == '__main__':
    w = WebConfig('test')
    _driver = w.get_driver_headless
    b = BaiduSearchBusiness(_driver)
    reslut_ele = b.baidu_searching('test')
    print(reslut_ele.text)
