#assert true
#when we have only two parameters we can use assertEqual method to check
#weather both are same or not, but we have more than two parameters, compairing values with assertEqual
#method become more difficult

#assert true method checks weather given parameter is true or not,
#if value is true then is passed otherwise test is failed

#assert false
#assertfalse method compares whether given value or expression result in false or not
#if the result or value is false then unittest passes the testcase
#but if the result or value is true then unittest fails the test case

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="D:/appium/chromedriver.exe")
        driver.get("https://google.com")
        titleofwebpage = driver.title
        self.assertTrue(titleofwebpage == "Google")  #true
if __name__ == "__main__" :
    unittest.main()

