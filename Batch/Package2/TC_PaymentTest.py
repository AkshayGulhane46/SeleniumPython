import unittest
class PaymentTest(unittest.TestCase):

    def test_PaymentInDoller(self):
        print("this is payment in doller test")
        self.assertTrue(True)

    def test_PaymentInRupee(self):
        print("this is payment in Rupee test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()