import pytest


@pytest.mark.finish
def testmark():
    assert 1 == 1

@pytest.mark.unfinish
def testmark2():
    assert 1==2



# pytest -m finish