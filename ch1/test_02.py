import pytest


# @pytest.mark.xfail
def test_failing():
    expected = (3, 2, 1)
    actual = (1, 2, 3)
    assert actual == expected
