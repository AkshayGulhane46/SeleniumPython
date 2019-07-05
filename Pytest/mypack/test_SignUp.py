import pytest

@pytest.yield_fixture()
def setup():
    print("oprning url to signup")
    yield
    print(" closing browser after signup")

def test_signupbyemail(setup):
    print("this is signup by email test")

def test_signupbyfacebook(setup):
    print("this is signup by facebook test")

