import requests
import pprint

def test_request():
    response = requests.get('http://www.baidu.com')
    print(response.status_code)
    pprint.pprint(response.content)