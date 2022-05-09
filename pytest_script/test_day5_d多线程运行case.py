'''
当cases量很多时，运行时间也会变的很长，如果想缩短脚本运行的时长，就可以用多进程来运行。
安装pytest-xdist：pip install -U pytest-xdist
运行模式：
pytest test_se.py -n NUM(其中NUM填写并发的进程数。)
'''
import pytest


def test_demo1():
    assert 1 == 1


def test_demo2():
    assert 1 == 2


def test_demo3():
    assert 1 == 1


def test_demo4():
    assert 1 == 2


def test_demo5():
    assert 1 == 1


def test_demo6():
    assert 1 == 2


def test_demo7():
    assert 1 == 1


def test_demo8():
    assert 1 == 2


def test_demo9():
    assert 1 == 1


def test_demo0():
    for i in range(100000):
        print(i)

    assert 1 == 1


if __name__ == '__main__':
    pytest.main('vs','-n 4',[__file__])
