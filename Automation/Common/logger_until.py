from Common.yaml_until import YamlUtil
import logging.config
import time
from Common.root_until import RootUntil


class Logger:

    def __init__(self):
        self._root = RootUntil()
        self._configpath = self._root.get_configfile[2]['Logger']
        self._configpath['handlers']['fileHandler'][
            'filename'] = self._root.get_rootpath + '/Log/TestDemoApi_' + time.strftime('%Y%m%d')
        logging.config.dictConfig(self._configpath)
        self._logger = logging.getLogger('applog')

    def logger(self, _message):
        self._logger.info(_message)

    def logger_error(self, e):
        return self._logger.exception(e)

    def logger_debug(self, message):
        return self._logger.debug(message)
