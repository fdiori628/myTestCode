import time
import os
from Common.root_until import RootUntil
from Common.logger_until import Logger
import subprocess
from Common.email_until import Email



class Run:
    # '/htmlReport/allure_temp', '/htmlReport/Allure_Reports'
    def __init__(self, run_path, report_path, reruns="3", level=None, report_temp=""):
        self.log = Logger()
        self.cmd = os.system
        self._run_path = run_path
        self.timeStr = time.strftime('%Y%m%d%H%M%S')
        self._reportTemp = RootUntil().get_rootpath + report_temp + '/ESB_AutomationTestReport_' + self.timeStr
        self._reportPara = '--alluredir=' + self._reportTemp
        self._report_path = RootUntil().get_rootpath + report_path + '/ESB_AutomationTestReport_' + self.timeStr
        self.level = level
        self.reruns = reruns

    def runTest(self):
        print(self._report_path)
        reportPath = RootUntil().get_rootpath + "/Report/htmlReport"
        cmdMv = "cp -rf " + reportPath + "/*.html" + " " + RootUntil().get_rootpath + "/Report/htmlReport/history"
        cmdDe = "rm -rf " + reportPath + "/*.html"
        print(cmdMv)
        os.system(cmdMv)
        time.sleep(1)
        os.system(cmdDe)
        cmd = ''
        time.sleep(1)
        if self.level is not None:
            cmd = "pytest " + self._run_path +\
                  " -m " + self.level + " --reruns " + self.reruns + " --html=" +\
                  self._report_path + ".html" + " --self-contained-html"
        else:
            cmd = "pytest " + self._run_path + " --reruns " + self.reruns +\
                  " --html=" + self._report_path + ".html" + " --self-contained-html"
        os.system(cmd)
        # cmdStatus = p.wait()
        # time.sleep(5
        # self.sendMail()

    # def sendMail(self):
    #     smtp = 'smtp.163.com'
    #     pop = 'pop.163.com'
    #     emailaddr = 'essex_automation@163.com'
    #     token = 'RNRIYKBJMEPZGTQK'
    #     e = Email(smtp=smtp, emailaddr=emailaddr, pwd=token, pop3=pop)
    #     subject = 'ESB_AutomationTestReport_' + self.timeStr
    #     _from = 'Xingyang Han'
    #     _to = ['xingyang.han@essexlg.com']
    #     msg_content = "Please find the ESB automation test report as attachment"
    #     attachment = {
    #         'maintype': 'html',
    #         'subtype': 'html',
    #         'filename': 'ESB_AutomationTestReport_' + self.timeStr,
    #         'filepath': self._report_path
    #     }
    #     e.send_email(subject=subject, _from=_from, _to=_to, content=msg_content, attachment=attachment)
    # def run_tests(self):
    #     self.log.logger(f'Testing for {self._run_path} is loading')
    #     pytest.main(['-v', self._run_path, self._reportPara])
    #     self.cmd('allure generate ' + self._reportTemp + ' -o ' + self._report_path)

    # def del_report_temp(self):
    #     self.cmd('cd htmlReport/allure_temp && rm -rf *')
    #     self.log.logger(f'report_temp folder is cleared')
    #
    # def del_report(self):
    #     self.cmd('cd htmlReport/Allure_Reports && rm -rf *')
    #     self.log.logger(f'report folder is cleared')


if __name__ == '__main__':
    run_path = 'testCase/PivotTable/Properties/test_value.py'
    # report_temp = '/htmlReport/allure_temp'
    report_path = '/Report/htmlReport'
    r = Run(run_path, report_path)
    r.runTest()
    # # r.del_report_temp()
    # # r.del_report()
