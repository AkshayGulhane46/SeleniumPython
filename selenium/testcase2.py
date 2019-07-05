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