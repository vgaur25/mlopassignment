

from  src.math_operation import add, sub


def test_add():
    assert add(2, 5)==7
    assert add(-1, 1)==0
    assert add(6, 1)==7


def test_sub():
    assert sub(5, 3)==2
    assert sub(4, 3)==1
    assert sub(3, 3)==0
    assert sub(2, 3)==-1
