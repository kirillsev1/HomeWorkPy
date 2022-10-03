"""Test function findingpercent."""
from findpercent import findingpercent
import pytest

test_find = [('ABc dbE FRl Ama', '50%'), ('NDp Lka nuR vtE', '25%')]


@pytest.mark.parametrize('string, answer', test_find)
def test_finder(string, answer):
    """
    Test function with tuples with answers.

    Args:
        string: tuple - tuple with input and output.
        answer: str - percents.
    """
    assert findingpercent(string) == answer
