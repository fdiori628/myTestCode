from Common.yaml_until import YamlUtil
import pytest
from POM.Business import baidu_Search_Business


class TestBaiduSearch:

    testData = YamlUtil('../Resource/test_demo_baidu/testSelenium_Data.yaml').read_yaml()
    searchData = testData["test_search_data"]

    @pytest.mark.parametrize('inputvalue', searchData)
    def testsarch(self, inputvalue):
        content = baidu_Search_Business.baidu_search(inputvalue)
        assert inputvalue in content
