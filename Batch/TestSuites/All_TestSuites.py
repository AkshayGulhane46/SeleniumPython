import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignUpTest import SignUpTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest


# get all tests from logintest , signuptest, paymenttest and paymentreturn test

tc1= unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2= unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3= unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4= unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#creating test suites
#sanityTestSuite= unittest.TestSuite([tc1, tc2])
#unittest.TextTestRunner().run(sanityTestSuite)

#functionalTestSuite=unittest.TestSuite([tc3, tc4])
#unittest.TextTestRunner().run(functionalTestSuite)

masterTestSuite=unittest.TestSuite([tc1, tc2, tc3, tc4])   #it will run all test case
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)  #verbosity means






