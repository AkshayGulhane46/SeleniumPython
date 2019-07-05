#assertgreater
#verifies whether first values if greater than second value or not

#assertGreaterEqual
#verifies whether first parameter is greater or equal to the second parameter

#assertless
#verifies wheather first parameter is lesser than second parameter or not

#assertlessequal
#verifies wheather first parameter is lesser or equal to the second parameter



import unittest
class Test(unittest.TestCase):
    def testName(self):
        #self.assertGreater(100,10)   #if first value is greater than second value then it is true
        self.assertGreaterEqual(100,10) #greater than equal to
        self.assertLess(200,20)#less than first number #failed
        self.assertLessEqual(200,300)#equal or less than first numbrer
    if __name__ =="__main__":
        unittest.main()