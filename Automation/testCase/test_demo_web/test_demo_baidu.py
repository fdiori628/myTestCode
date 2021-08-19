import pytest
from POM.Business.test_demo_baidu.baidu_Search_Business import BaiduSearchBusiness
from Common.web_config_until import WebConfig


class TestBaiduSearch:
    config = WebConfig('test_demo_baidu')
    testdata = config.testdata['test_search_data']

    @pytest.mark.parametrize('testdata', testdata)
    def testsarch(self, testdata, driver_headless):
        testresult = BaiduSearchBusiness(driver_headless).baidu_searching(testdata).text
        assert testdata in testresult


