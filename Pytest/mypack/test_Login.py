import pytest

@pytest.yield_fixture()
def setup():
    print("opening URL to Login")
    yield
    print("closing browser after login")

def test_LoginByEmail(setup):
    print("This is login by email test ")

def test_LoginByFacebook(setup):
    print("this is login by facebook test ")