# python unittest HTML testrunner reports
# selenium python test case using unit test, html reports
# selenium python project unittest,page object model (pom) ,html reports
#
# html test runner installer
# c\windows\system32\>pip install html-testRunner
#
# 1 launch browse
# 2 verify home page title
# 3 verify login
# 4 close browser
#
#setUpClass
#tearDownClass
#both are not normal methods these are fixtures


import unittest
from selenium import webdriver
import HtmlTestRunner   #To generate test reports this is used



class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/appium/chromedriver.exe")
        cls.driver.maximize_window()

# setUp is a predefined function
# cls is a default parameter like self
# if we create a function within a class then cls is called
# functions can be made without class
#if we insert same function within class then it is called method



    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM32",self.driver.title,"webpage title is not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.driver.get("https://opensource-demo.orangehrmlive.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed.......")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C://Users/Android - PC//PycharmProjects//UnitTest+htmlreports+pom//Report'))

        #unittest.main()
        #insted of these command pass a parameter
        #to run this test case first make a directory called as Reports
        #run this program on terminal by writing python  TestCase_Orange_HRM_Login.py


#
# #from here we will use page object model (POM)
# #Image result for page object modelwww.guru99.com
# # Page Object Model is a design pattern which has become popular in test automation for
# # enhancing test maintenance and reducing code duplication.
#
# if we have multiple test cases and multiple pages in application
# in first teast case we should able to identify other test cases pages
# problem is repetation as each page element is identified by every test case
# this problem we have in normal approach
# here if one page is modified we have to change every connection
#
# so using POM we can seprete them test methods are different and page elements are different
# for every page in application i will create one seprate file this is also a python file
# and this file contain only elements and action methods means to perform certain operations on this
# action means what are operations we are going to do on this element
#
#






