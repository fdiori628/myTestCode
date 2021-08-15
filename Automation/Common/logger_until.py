from Common.yaml_until import YamlUtil
import logging.config
import time


class Logger:

    def __init__(self):
        self._configpath = YamlUtil('./Config.yaml').read_yaml()[2]['Logger']
        self._configpath['handlers']['fileHandler']['filename'] = './Log/TestDemoApi_' + time.strftime('%Y%m%d')
        logging.config.dictConfig(self._configpath)
        self._logger = logging.getLogger('applog')

    def logger(self, _message):
        self._logger.info(_message)

    def logger_error(self, e):
        return self._logger.exception(e)

    def logger_debug(self, message):
        return self._logger.debug(message)
