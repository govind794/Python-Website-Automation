import unittest
import os
from TestCase.test_HomePage import HomePage
from TestCase.test_AddToCartAndPayment import AddToCartAndPayment

tc1 = unittest.TestLoader().loadTestsFromTestCase(HomePage)
tc2 = unittest.TestLoader().loadTestsFromTestCase(AddToCartAndPayment)

senityTestSuites = unittest.TestSuite([tc1])
funTestSuites = unittest.TestSuite([tc2])
masertTestSuites = unittest.TestSuite([tc1, tc2])

# unittest.TextTestRunner().run(senityTestSuites)
# unittest.TextTestRunner().run(funTestSuites)
unittest.TextTestRunner(verbosity=2).run(masertTestSuites)
