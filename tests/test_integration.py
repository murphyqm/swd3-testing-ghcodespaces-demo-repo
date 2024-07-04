from hypot.calc import pythag
import pytest

# test pythag

def test_pythag_zero():
    assert pythag(0, 0) == 0
    
def test_pythag_int():
    assert pythag(3, 4) == 5

def test_pythag_neg():
    assert pythag(-3, 4) == 'Sides of the triangle must be positive'

def test_pythag_float():
    assert pythag(7.5, 9.14) == pytest.approx(11.823265200442727)