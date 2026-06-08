import pytest

@pytest.mark.regression
def test_sample1():
    print("sample1")

@pytest.mark.regression
def test_sample2():
    num=[1,2,3,4,5]
    x=2
    assert x in num
    print("sample2")
@pytest.mark.smoke

def test_sample3():
    x=5
    y=10
    assert x<y
    print("sample3")

@pytest.mark.xfail
@pytest.mark.smoke
def test_string():
    a="arun"
    b="arun"
    assert a.__eq__(b)
    assert a==b


@pytest.mark.parametrize("act,exp",[(1,1),(2,3),(3,3)])
@pytest.mark.compar
def test_mark(act,exp):
    assert act==exp
