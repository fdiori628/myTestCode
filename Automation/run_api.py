import pytest
import time


t = time.strftime('%Y%m%d%H%M%S')
repotpath = "--html=./Report/test_report_api/" + 'TestReport_API_' + t + ".html"

if __name__ == '__main__':
    pytest.main(['-s', '--reruns=3', './testCase/test_demo_api', repotpath, '--self-contained-html'])
