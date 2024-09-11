import pytest
def test_01():
    a = 10
    b = 23
    assert a != b, 'Test is failed'

def test_02():
    c = 10
    d = 10
    assert c == d, 'Test is failed'

@pytest.mark.login
def test_Login():
    assert True