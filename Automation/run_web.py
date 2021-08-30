import pytest
import time

t = time.strftime('%Y%m%d%H%M%S')
repotpath = "--html=./Report/test_report_web/" + 'TestReport_Web_' + t + ".html"
if __name__ == '__main__':
    pytest.main(['-v', './testCase/test_demo_web', repotpath, '--self-contained-html'])