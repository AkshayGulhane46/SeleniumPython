#python unit testing framework
#skipping tests
#skip tests
#skip test with reasons
#skip test based on condition

import unittest
class Apptesting(unittest.TestCase):

    @unittest.SkipTest   #this will ignore this specific test
    def test_search(self):
        print("this is search test")

    @unittest.skip("I am skipping this test method because it is not yet ready")
    #this will show skipping message with skip
    def test_advancesearch(self):
        print("this is advance search method")

    @unittest.skipIf(1==1,"ONE IS EQUALS TO ONE")  #if condition is false then why its is false will be written in message
    def test_prepaidreacharge(self):

        print("this is pre-paid test case")

    def test_postpaidreacharge(self):
        print("this is postpaid reacharge test")

    def test_loginbygmail(self):
        print("this is login by gmail")

    def test_loginbytwitter(self):
        print("this is login by twitter")

if __name__== "__main__":
    unittest
