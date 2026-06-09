import pytest_check as check

def test_soft_assert():

    print("Step 1")
    check.equal(1, 1)

    print("Step 2")
    check.equal(2, 2)

    print("Step 3")
    check.equal(3, 3)


    print("step4")
    check.equal("jeeva","jeeva")
    check.greater_equal(10,1)
    check.greater(100,9)
    check.less(1,10)

    print("Test Completed")
