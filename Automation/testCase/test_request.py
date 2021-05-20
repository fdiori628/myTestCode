import requests


def test_request():
    response = requests.get('http://www.baidu.com')
    print(response.status_code)