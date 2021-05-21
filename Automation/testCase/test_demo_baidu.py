import yaml
import pytest
import sys
sys.path.append('../POM/')
import baidu_Search_Business


class TestCase:
    testdataFile = open('../Resource/test_demo_baidu/testSelenium_Data.yaml', 'r')
    testData = yaml.load(testdataFile, Loader=yaml.FullLoader)
    searchData = testData["test_search_data"]

    def setup(self):
        self.baidu_Search = baidu_Search_Business.baidu_search

    def teardown(self):
        print('this is teardown')

    @pytest.mark.parametrize('inputValue', searchData)
    def testSearch(self, inputValue):
        self.baidu_Search(inputValue)
