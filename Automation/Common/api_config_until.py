from Common.yaml_until import YamlUtil
from string import Template


class ApiConfig:

    def __init__(self, api_name):
        self._apiname = api_name
        self._api = YamlUtil('../../../Config.yaml').read_yaml()[0]['API']

    def get_apiinfo(self):
        try:
            info_list = list(self._api.keys())
            tempdict = {}
            for i in info_list:
                if i == 'Domain':
                    pass
                else:
                    temp = Template(self._api[i])
                    api_name = {
                        "apiname": self._apiname
                    }
                    result = temp.substitute(api_name)
                    tempdict[i] = result
            return tempdict
        except Exception as e:
            raise e

    @property
    def all(self):
        return self._api

    @property
    def domain(self):
        return self._api['Domain']

    @property
    def report_path(self):
        report_path = ApiConfig(self._apiname).get_apiinfo()
        return report_path['ReportPath']

    @property
    def apiconfig_path(self):
        report_path = ApiConfig(self._apiname).get_apiinfo()
        return report_path['ConfigPath']

    @property
    def testdata_path(self):
        report_path = ApiConfig(self._apiname).get_apiinfo()
        return report_path['TestDataPath']
