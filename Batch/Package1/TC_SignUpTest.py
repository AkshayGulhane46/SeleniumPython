import unittest
class SignUpTest(unittest.TestCase):
    def test_SignUpByEmail(self):
        print("This is signup by email test ")
        self.assertTrue(True)

    def test_SignUpByFacebook(self):
        print("this is signup by facebook")
        self.assertTrue(True)

    def test_SignUpByTwitter(self):
        print("this is signup by Twitter")
        self.assertTrue(True)

if __name__ == "__ main __ ":
    unittest.main()