from Common.yaml_until import YamlUtil
from string import Template
from Common.root_until import RootUntil
from Common.logger_until import Logger


class WebConfig:

    def __init__(self, app_name):
        self._app_name = app_name
        self._root = RootUntil()
        self._appconfig = self._root.get_configfile[0]['WEB']
        self._rootpath = self._root.get_rootpath
        self._log = Logger()
        self._config = self._root.get_configfile
        self.env = self._root.get_configfile[2]['ENV']

    def get_appinfo(self):
        try:
            info_list = list(self._appconfig.keys())
            tempdict = {}
            for i in info_list:
                temp = Template(self._appconfig[i])
                appname = {
                    "appname": self._app_name,
                    "rootpath": self._rootpath
                }
                result = temp.substitute(appname)
                tempdict[i] = result
            # self._log.logger_debug(f'The config info is {tempdict}')
            return tempdict
        except Exception as e:
            raise e and self._log.logger_error(e)

    def get_env_info(self, env):
        return self.env[env]

    @property
    def report_cmd(self):
        path = WebConfig(self._app_name).get_appinfo()
        return path['ReportPath']

    @property
    def testdata(self):
        path = WebConfig(self._app_name).get_appinfo()['TestDataPath']
        data = YamlUtil(path).read_yaml()
        return data

    @property
    def domelements(self):
        path = WebConfig(self._app_name).get_appinfo()['DomElement']
        elements = YamlUtil(path).read_yaml()
        return elements

    @property
    def pom_business_path(self):
        path = WebConfig(self._app_name).get_appinfo()['POM_business_path']
        return path


if __name__ == '__main__':
    w = WebConfig('Properties_common/values')
    t  = w.testdata
    print(env217)
