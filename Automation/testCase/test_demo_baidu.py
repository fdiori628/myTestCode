import yaml
import pytest
import sys
sys.path.append('../POM/')
import baidu_Search_Business


class TestCase:
    testdataFile = open('../Resource/test_demo_baidu/testSelenium_Data.yaml', 'r')
    testData = yaml.load(testdataFile, Loader=yaml.BaseLoader)
    searchData = testData["test_search_data"]

    @pytest.mark.parametrize('inputValue', searchData)
    def testsarch(self, inputValue):
        content = baidu_Search_Business.baidu_search(inputValue)
        assert inputValue in content
