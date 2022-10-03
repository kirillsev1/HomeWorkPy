"""Test function."""
from datefunc import check
import pytest

test_date = [('29.02.2002', False), ('12.12.-1100', True), ('12.20.2002', False)]


@pytest.mark.parametrize('string, answer', test_date)
def test_datestring(string, answer):
    """
    Test function by tuples with answers.

    Args:
        string: tuple - tuple with input and output.
        answer: str - percents.
    """
    assert check(string) == answer
