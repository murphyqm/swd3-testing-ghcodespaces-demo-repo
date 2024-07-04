from hypot.calc import squared, addition, sqroot

# test squared
def test_squared_even():
    assert squared(2) == 4


def test_squared_odd():
    assert squared(3) == 9


def test_squared_zero():
    assert squared(0) == 0


# test addition

def test_addition_even():
    assert addition(2, 4) == 6


def test_addition_odd():
    assert addition(3, 5) == 8


def test_addition_mix():
    assert addition(2, 5) == 7


def test_addition_zero():
    assert addition(2, 0) == 2


# test sqroot


def test_sqroot_even():
    assert sqroot(4) == 2


def test_sqroot_odd():
    assert sqroot(9) == 3


def test_sqroot_zero():
    assert sqroot(0) == 0