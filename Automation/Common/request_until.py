import requests
import json


class RequestUtil:

    def __init__(self, method, url, **kwargs):
        self._method = method
        self._url = url
        self._kwargs = kwargs
        self.session = requests.session()

    def send_request(self):
        method = str(self._method).lower()
        try:
            res = self.session.request(method, self._url, **self._kwargs).text
            res = json.loads(res)
            return res
        except TimeoutError as e:
            raise e
