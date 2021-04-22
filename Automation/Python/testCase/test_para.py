import pytest


# the pwd will be tested by 3 times for it's length
@pytest.mark.parametrize('pwd', [
    '123456344', 'abcdefgas', 'bnsdasdksd'
])
def testpara_pwd(pwd):
    assert len(pwd) > 8
