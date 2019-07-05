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

-------------------------------------------------------main program---------------------------------------------------

import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_google(self):  #self means this perticular variable is belongs to this method
        self.driver=webdriver.Chrome(executable_path="D:/appium\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("title of page is" + self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="D:/appium\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("title of page is "+ self.driver.title)
        self.driver.close()

if __name__=="__main__":
    unittest.main()