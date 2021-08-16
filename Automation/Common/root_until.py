import os
import re


class RootUntil:

    def __init__(self):
        self._root = os.getcwd()
        self._projectroot = self._root[0: re.search('Automation', self._root).span()[1]]

    @property
    def get_rootpath(self):
        return self._projectroot

    @property
    def get_driver(self):
        driver_path = '\\Drivers\\chromedriver.exe'
        return self._projectroot + driver_path

    @property
    def get_configfile(self):
        file_path = '\\Config.yaml'
        return self._projectroot + file_path
