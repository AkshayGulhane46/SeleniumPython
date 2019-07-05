import pytest


@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield                                       #as there are two statements in fixture
                                                #and in the middle there is yield
                                                #first , first statement execute then testcase1 will execute and then second method is executed
    print("once after every method")


def testMethod1(setup):
    print("this is test method 1")

def testMethod2(setup):
    print("this is test method 2")
