import pytest
import time
import os
from Common.root_until import RootUntil
from Common.logger_until import Logger


class Run:
    # '/htmlReport/allure_temp', '/htmlReport/Allure_Reports'
    def __init__(self, run_path, report_temp, report_path):
        self.log = Logger()
        self.cmd = os.system
        self._run_path = run_path
        timeStr = time.strftime('%Y%m%d%H%M%S')
        self._reportTemp = RootUntil().get_rootpath + report_temp + '/TestReport_' + timeStr
        self._reportPara = '--alluredir=' + self._reportTemp
        self._report_path = RootUntil().get_rootpath + report_path + '/TestReport_' + timeStr

    def run_tests(self):
        self.log.logger(f'Testing for {self._run_path} is loading')
        pytest.main(['-v', self._run_path, self._reportPara])
        self.cmd('allure generate ' + self._reportTemp + ' -o ' + self._report_path)

    def del_report_temp(self):
        self.cmd('cd htmlReport/allure_temp && rm -rf *')
        self.log.logger(f'report_temp folder is cleared')

    def del_report(self):
        self.cmd('cd htmlReport/Allure_Reports && rm -rf *')
        self.log.logger(f'report folder is cleared')


if __name__ == '__main__':
    run_path = 'testCase/Login'
    report_temp = '/htmlReport/allure_temp'
    report_path = '/htmlReport/Allure_Reports'
    r = Run(run_path, report_temp, report_path)
    r.run_tests()
    # r.del_report_temp()
    # r.del_report()
