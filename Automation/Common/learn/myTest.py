import requests
from Common.yaml_until import YamlUtil
import pytest


class TestDemo:
    data = YamlUtil('myfile.yaml').read_yaml()

    def setup(self):
        self.url = 'http://localhost:3000/posts'

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
            response = requests.request(method, url, params=parm, headers=header)
            context = response.json()
            assert context[0]['id'] == data['validation']['id']
        else:
            requestdata = data['requestdata']['data']
            print('TestCase %s is starting' % name)
            response = requests.request(method, url, data=requestdata)
            context = response.json()
            assert context['title'] == requestdata['title'], context['author'] == requestdata['author']
