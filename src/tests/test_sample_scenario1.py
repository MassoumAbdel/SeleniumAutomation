import pytest

print("Starting the sample test scenario.")


@pytest.fixture(scope='module')
def greet():
    print("Hellooooooooo Test Master!")
    return [2,3,4]

@pytest.mark.scen1
@pytest.mark.scen1case1
def test_scen1_case1(greet):
    print("scenario 1 case 1 staring ..")
    print(greet)
    greet.append(5)
    print(greet)
    assert 'hello' == 'hello'

# @pytest.mark.skip
@pytest.mark.scen1
@pytest.mark.smoketest
@pytest.mark.scen1case2
def test_scen1_case2(greet):
    print("scenario 1 case 2 staring ..")
    print(greet)
    greet.append(6)
    print(greet)
    assert 2 == 3 , "case 2 failed"







