from sqlite3 import connect

import pytest

a = 10
b = 20


def test_raise():
    with pytest.raises(TypeError) as e:
        connect('localhost', '1234')
    exec_msg = e.value.args[0]
    assert exec_msg == 'must be real number, not str'

