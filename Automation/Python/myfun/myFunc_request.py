import requests


class Myfunc:

    def __init__(self):
        self.response = requests.get('http://www.baidu.com')

    def myfunc_request(self):
        print(self.response.status_code)


m = Myfunc()

m.myfunc_request()
