import yaml
import pytest
import sys

sys.path.append('../POM/')
import baidu_Search_Business

testdataFile = open('../Resource/test_demo_baidu/testSelenium_Data.yaml', 'r')
testData = yaml.load(testdataFile, Loader=yaml.FullLoader)
searchData = testData["test_search_data"]
baidu_Search = baidu_Search_Business.baidu_search


@pytest.mark.parametrize('inputValue', searchData)
def test_search(inputValue):
    baidu_Search(inputValue)
