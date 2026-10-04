import pytest
from src.calculator import fun1, fun2, fun3, fun4

def test_fun1():
    assert fun1(2, 3) == 5

def test_fun2():
    assert fun2(5, 3) == 2

def test_fun3():
    assert fun3(2, 3) == 6

def test_fun4():
    assert fun4(2, 3) == 10

@pytest.mark.parametrize("x, y, expected", [
    (0, 0, 0),
    (1, 1, 3),
    (-1, 1, -1),
])
def test_fun4_parametrized(x, y, expected):
    assert fun4(x, y) == expected
