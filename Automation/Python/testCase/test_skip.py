import pytest


@pytest.mark.skip(reason='test')
def testskip():
    assert 1 == 2
