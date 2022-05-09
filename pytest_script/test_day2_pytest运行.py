import pytest


def test_demo1():
    assert 1 == 1


def test_demo2():
    assert 1 == 2


if __name__ == '__main__':
    pytest.main('vs', [__file__])
