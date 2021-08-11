import time
import pytest

t = time.strftime("%Y-%m-%d %H:%M:%S")


@pytest.fixture(scope='function')
def con_database():
    print('connecting database  %s' % t)
    con_id = 1
    return con_id
