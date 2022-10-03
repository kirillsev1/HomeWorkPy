"""Testing function"""
from datefunc import check
import pytest

test_date = [('29.02.2002', False), ('12.12.-1100', True), ('12.20.2002', False)]

@pytest.mark.parametrize('string, result', test_date)
def test_datefunc(string, result):
    assert check(string) == result
