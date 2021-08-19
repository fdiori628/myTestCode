from Common.yaml_until import YamlUtil
from string import Template
from Common.root_until import RootUntil


class ApiConfig:

    def __init__(self, api_name):
        self._apiname = api_name
        self._root = RootUntil()
        self._api = self._root.get_configfile[0]['API']
        self._rootpath = self._root.get_rootpath

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
                        "apiname": self._apiname,
                        "rootpath": self._rootpath
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
        return self._rootpath + report_path['ConfigPath']

    @property
    def testdata_path(self):
        report_path = ApiConfig(self._apiname).get_apiinfo()
        return self._rootpath + report_path['TestDataPath']


a = ApiConfig('test_demo_api1')

print(a.testdata_path)
print(a.apiconfig_path)
print(a.report_path)
