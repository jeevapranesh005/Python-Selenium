import pytest

@pytest.mark.regression
@pytest.mark.order(3)
def test_sample1():
    print("sample1")

@pytest.mark.regression
@pytest.mark.order(2)
def test_sample2():
    num=[1,2,3,4,5]
    x=2
    assert x in num
    print("sample2")


@pytest.mark.smoke
@pytest.mark.order(1)
def test_sample3():
    x=5
    y=10
    assert x<y
    print("sample3")


@pytest.mark.order(4)
@pytest.mark.xfail
@pytest.mark.smoke
def test_string():
    a="arun"
    b="arun"
    assert a.__eq__(b)
    assert a==b


@pytest.mark.order(5)
@pytest.mark.parametrize("act,exp",[(1,1),(2,2),(3,3)])
@pytest.mark.compar
def test_mark(act,exp):
    assert act==exp
