import operator
import pytest

def test_add():
    assert operator.add(1, 2) == 3

def test_minus():
    assert operator.minus(2, 1) == 1