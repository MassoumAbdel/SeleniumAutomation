import pytest

@pytest.mark.smoketest
@pytest.mark.scen2case1
def test_scen2_case1():
    print("\nscenario 2 case 1 starting ..")
    assert True


@pytest.mark.scen2case2
def test_scen2_case2():
    print("\nscenario 2 case 2 starting ..")
    assert False


