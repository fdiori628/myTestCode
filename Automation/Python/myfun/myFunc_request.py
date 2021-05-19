import requests


class Myfunc:

    def __init__(self):
        self.response = requests.get('http://www.baidu.com')

    def myfunc_request(self):
        print(self.response.status_code)

    def myfunc_test(self):
        self.a = "abcde"
        assert "a" in self.a


m = Myfunc()

m.myfunc_test()
