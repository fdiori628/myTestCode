import os
import re
from Common.yaml_until import YamlUtil


class RootUntil:

    def __init__(self):
        self._root = os.getcwd()
        self._projectroot = self._root[0: re.search('EyeGuide_ESBAutomation', self._root).span()[1]]
        self._config = YamlUtil(self._projectroot + '/Config.yaml').read_yaml()

    @property
    def get_rootpath(self):
        return self._projectroot

    # @property
    # def get_driver(self):
    #     driver_path = self._driverpath
    #     driverm1_path = self._driverm1path
    #     return self._projectroot + driver_path

    @property
    def get_configfile(self):
        file_path = self._projectroot + '/Config.yaml'
        file = YamlUtil(file_path).read_yaml()
        return file
