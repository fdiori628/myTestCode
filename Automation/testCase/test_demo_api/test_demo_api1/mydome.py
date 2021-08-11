from Common.yaml_until import YamlUtil
from Common.api_config_until import ApiConfig
from Common.request_until import RequestUtil
import pytest


class TestApi1:
    config = ApiConfig('test_demo_api1')
    api_config = YamlUtil(config.apiconfig_path).read_yaml()
    domain = api_config['Domain']
    testdata = YamlUtil(config.testdata_path).read_yaml()

    def setup(self):
        self.send_request = RequestUtil

    @pytest.mark.parametrize('testdata', testdata)
    def test_get(self, con_database, testdata):
        parm = testdata['requestdata']['param']
        method = testdata['requestdata']['method']
        url = TestApi1.domain + testdata['requestdata']['path']
        header = {
            'Content-Type': 'application/json'
        }
        name = testdata['name']
        if method == 'get':
            print('TestCase %s is starting' % name)
            response = self.send_request(method, url, params=parm, headers=header).send_request()
            assert response[0]['id'] == testdata['validation']['id']
        else:
            requestdata = testdata['requestdata']['data']
            print('TestCase %s is starting' % name)
            response = self.send_request(method, url, data=requestdata).send_request()
            assert response['title'] == requestdata['title'], response['author'] == requestdata['author']
