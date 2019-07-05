#assertisnone
#assertisnone method verifies whether give values or expression result in none or not
#if the result is none then python unittest will pass the test case
#otherwise fails the test case

#assertIsNotNone
#if the value is none then the test will be failed

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="D:/appium\chromedriver.exe ")
        #driver.get("https//:google.com")
        # self.assertIsNone(driver)   #check varible contain value or not  if __name__ == "__main__":
        #unittest.main(driver)             #should it contain none or not
        self.assertIsNotNone(driver)

if __name__ == "__main__":
    unittest.ma