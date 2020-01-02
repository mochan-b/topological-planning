
# Just refreshing the unit testing frameworks for python

import pytest

# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4