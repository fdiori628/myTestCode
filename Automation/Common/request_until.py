import requests
import json
from Common.logger_until import Logger


class RequestUtil:

    def __init__(self, method, url, **kwargs):
        self._method = method
        self._url = url
        self._kwargs = kwargs
        self.session = requests.session()

    def send_request(self):
        method = str(self._method).lower()
        requestdata = {
            "method": self._method,
            "others":self._kwargs
        }
        try:
            Logger().logger(f'Calling {self._url} with requestinfo: {requestdata}')
            res = self.session.request(method, self._url, **self._kwargs).text
            res = json.loads(res)
            Logger().logger(f'Get response: {res}')
            return res
        except TimeoutError as e:
            raise e
