import unittest
class LoginTest(unittest.TestCase):
    def test_LoginByEmail(self):
        print("This is login by email test ")
        self.assertTrue(True)

    def test_LoginByFacebook(self):
        print("this is login by facebook")
        self.assertTrue(True)

    def test_LoginByTwitter(self):
        print("this is login by Twitter")
        self.assertTrue(True)

if __name__ == "__ main __ ":
    unittest.main()