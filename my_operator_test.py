import my_operator
import pytest

def test_add():
    assert my_operator.add(1, 2) == 3

def test_minus():
    assert my_operator.minus(2, 1) == 1

def test_mod():
    assert my_operator.mod(10, 3) == 1