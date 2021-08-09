import pytest
import time

t = time.strftime('%Y%m%d%H%M%S')
repotpath = "--html=./Report/" + t + ".html"

if __name__ == '__main__':
    pytest.main(['-vs', '--reruns=3', 'myTest.py', repotpath, '--self-contained-html'])
