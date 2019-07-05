

#before comming here please refer old program where the basic commands are explained
######
#####
####
###
##
#
import unittest
import HtmlTestRunner
from selenium import webdriver
import time

#for setting environment variables this is needed
import sys
sys.path.append("C:/Users/Android - PC/PycharmProjects/POMBased")
#this environment variable is like regular environment variable that you set in my computer
from PageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL="http://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"
    driver=webdriver.Chrome(executable_path="C:\\Users\\Android - PC\\PycharmProjects\\POMBased\\Drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)  #here cls is representing the class as you using class variable
        cls.driver.maximize_window()


    def test_login(self):
        lp=LoginPage(self.driver)  #object created for loginpage
                                       #and initiated the driver
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard/nopCommerce administration",self.driver.title,"webpage title is not matching ")

    # by writing cls this is a class level method
    @classmethod
    def tearDownClass(cls):
            cls.driver.close()

if  __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users\Android - PC\PycharmProjects\POMBased\Reports'))


