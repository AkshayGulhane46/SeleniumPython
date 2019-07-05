import unittest
from selenium import webdriver

class Test (unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="D:/appium/chromedriver.exe")
        driver.get("https://www.google.com/")
        titleofwebpage = driver.title
        #assertEqual
        #self.assertEqual("Google", titleofwebpage, "webpage title is not same")
        self.assertNotEqual("Google", titleofwebpage)
if __name__ == " __main__ ":
    unittest.main()


#assertion in python
#assertion means a confident and forceful statement of fact or belief

#assertion is nothing but a checkpoint or you can say it is a verification for the test case to evaluate
#some items on the execution

#if we do not provide any assertion inside a test case then
#there is no way to know weather a test case is failed or not

#assertion helps in report generation based on the assertions
#the test execution report will be generated

#there are few assertions which will accept all the values
#and few asserions accept only numeric values

#assertEqual
#assert equal compares the first parameter with the second parameter if both matches
# the unittest will continue with the remaining execution but the both the values
#are different then unit test fails the testcase

#assertNotequal
#assert not equal methid compares the given two parameters if both parameters are not same
#then unit test passes the test case but if both parameters are same then unittest fails
#the test case
