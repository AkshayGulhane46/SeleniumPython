#how to work with pytest fixtures
#the purpose of test fixture is to provide a fixed baseline
#upon which tests can be repetedly execute


import pytest

@pytest.fixture()     #this is new here
def setup():
    print("executed once before every method ")

def testmethod1(setup):  #by wrinting setup this method execute setup before testmethod 1
    print("this is test method 1")

def testmethod2(setup):  #by wrinting setup this method execute setup before testmethod 2
    print("this is test method 2")

#this program also should be run through command prompt
#pytest -v -s test_pytestdemo1.py
#  -v for verbose
#  -s for print statements



