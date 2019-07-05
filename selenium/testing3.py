#setup method and teardown methods are the two methods that execute every time
#while unit testing for each method

import unittest

class AppTesting(unittest.TestCase):

    def setUpModule():
        print("setUpModule")

    @classmethod                     #decorator and setup is execute before all
    def setUp(self):                 #login is mendentory before any method and it run multiple time
        print("this is login test")

    @classmethod                        #decorator
    def tearDown(self):
        print("this is logout test")

    @classmethod
    def setUpClass(cls):                #execute once the class started
        print("Open Application")

    @classmethod
    def tearDownClass(cls):             #execute once the class completed
        print("close Application")

    def test_search(self):
        print("this is a search test")

    def test_advancedsearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("this is prepaid recharge test")

    def test_postpaidRecharge(self):
        print("this is postpaid recharge test")



