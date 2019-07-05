#python Unittest framework
#in automation testing organizing your code is very important and client expects us to write
#automation scripts according to the manual test cases

#we get good reporting structure if we can exactly map our
#automation code with manual test cases

#in python we can use unittest testing framework to organize our automation code and
#to extract reports
#to use the methods present in the unit test framework we have to extend the test cases class present in
#present in the unittest module


import unittest
class Test(unittest.TestCase):  #this is must written statement
    def test_firstTest(self):
        print("this is my first unit test case")

if __name__=="__main__":
    unittest.main()
