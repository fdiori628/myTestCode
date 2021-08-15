import json

from Common.yaml_until import YamlUtil
from Common.api_config_until import ApiConfig
from Common.request_until import RequestUtil
import pytest
from Common.logger_until import Logger


class TestApi1:
    apiname = 'test_demo_api1'
    config = ApiConfig(apiname)
    api_config = YamlUtil(config.apiconfig_path).read_yaml()
    domain = api_config['Domain']
    testdata = YamlUtil(config.testdata_path).read_yaml()

    def setup(self):
        self.send_request = RequestUtil
        self._apiname = TestApi1.api_config['ApiName']

    @pytest.mark.parametrize('testdata', testdata)
    def test_smoke(self, con_database, testdata):
        parm = testdata['requestdata']['param']
        method = testdata['requestdata']['method']
        url = TestApi1.domain + testdata['requestdata']['path']
        headers = testdata['requestdata']['headers']
        name = testdata['name']
        payload = testdata['requestdata']['data']
        func = lambda a, b: a if payload is None else b
        payload = func(None, json.dumps(payload))
        Logger().logger(f'{name} is starting')
        res = self.send_request(method, url, params=parm, headers=headers, data=payload).send_request()
        if method == 'get':
            assert res[0]['id'] == testdata['validation']['id']
        else:
            payload = json.loads(payload)
            assert res['title'] == payload['title'], res['author'] == payload['author']
