"""Testing function findingpercent"""
from findpercent import findingpercent
import pytest

test_find = [('ABc dbE FRl Ama', '50%'), ('NDp Lka nuR vtE', '25%')]

@pytest.mark.parametrize('testtuple, result', test_find)
def test_finder(testtuple, result):
    assert findingpercent(testtuple) == result