import pytest
from nicolascalclib import soma, subs, mult, divs, powX, pow2, raiz, rzqd

def test_add():
    assert soma(4, 3) == 7
    assert soma(-4, -3) == -7
    assert soma(0, 0) == 0

def test_subtract():
    assert subs(4, 3) == 1
    assert subs(0, -3) == 3

def test_multiply():
    assert mult(4, 3) == 12
    assert mult(-4, 3) == -12
    assert mult(4, 0) == 0

def test_divide():
    assert divs(4, 2) == 2
    assert divs(3, 3) == 1

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divs(4, 0)