import pytest

from sport.choices import BasePlayer

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_player():
    pass

# def test_an_another():
#     with pytest.raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
#         pass