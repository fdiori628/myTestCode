from Common.yaml_until import YamlUtil
from Common.request_until import RequestUtil
import pytest


class TestDemo:
    data = YamlUtil('myfile.yaml').read_yaml()

    def setup(self):
        self.url = 'http://localhost:3000/posts'
        self.send_request = RequestUtil

    @pytest.mark.parametrize('data', data)
    def test_get(self, con_database, data):
        parm = data['requestdata']['param']
        method = data['requestdata']['method']
        url = data['requestdata']['url']
        header = {
            'Content-Type': 'application/json'
        }
        name = data['name']
        if method == 'get':
            print('TestCase %s is starting' % name)
            response = self.send_request(method, url, params=parm, headers=header).send_request()
            assert response[0]['id'] == data['validation']['id']
        else:
            requestdata = data['requestdata']['data']
            print('TestCase %s is starting' % name)
            response = self.send_request(method, url, data=requestdata).send_request()
            assert response['title'] == requestdata['title'], response['author'] == requestdata['author']
