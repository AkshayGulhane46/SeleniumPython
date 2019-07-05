#assertIn
#method verifies whether the first element is present in the send element
#if the first element is present in second element then test is passed
#otherwise test is failed

#assertNotin
#method verifies whether the first element is not present in the second element or not
#if first element is present then test will be failed otherwise test is passed

#these two methods will be helpful when you want to verify presence of a value in a list
#tuple set and dictionary

import unittest

class Test(unittest.TestCase): #class test is extending unittest functionlaity
    def testName(self):
        list={"python","selenium","java"}
        #self.assertNotIn("python",list)returns false
        #self.assertNotIn("ruby",list)  returns true
        self.assertIn("python",list) #returns true and passed the test
if __name__ =="__main__":
    unittest.main()
