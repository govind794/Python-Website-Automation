'''
Author   : Govind Patidar
DateTime : 10/07/2020 11:30AM
File     : AddToCartAndPayment
'''

import unittest
import time
from Utility.browser_load import BrowserLoad
from Utility.logs import Logs
from PageObject.home_page import HomePageObject
from TestData.Moisturizes import Moisturize
from TestData.Sunscreens import Sunscreen
from TestData.AddCarts import AddCart
from TestData.CheckoutData import Checkout
from TestData.Payment import Payment

log = Logs(log="AddToCartAndPayment").getLogs()


class AddToCartAndPayment(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        '''
        #Load browser
        :return:
        '''
        print("-------Start Test Case--------")
        cls.browser = BrowserLoad(cls)
        cls.driver = cls.browser.browserOpen(cls)

    @classmethod
    def tearDownClass(cls):
        '''
        :return:
        '''
        print("--------Complate Test Case--------")
        cls.driver.quit()

    def test_AddToCartAndPayment(self):
        '''
        :return:
        '''
        # object class extend
        get_value = HomePageObject(self.driver)
        product_mois = Moisturize(self.driver)
        product_sun = Sunscreen(self.driver)
        cart = AddCart(self.driver)
        checkout = Checkout(self.driver)
        payment = Payment(self.driver)

        # get temperature value
        curr_temp = get_value.curr_temp()
        log.info(f"Get current Temp: {curr_temp}")

        # check condition on Temperature of sunscreens and moisturizes
        if int(curr_temp[:2]) <= 18:
            # click on button of Moisturizes
            get_value.buy_moisturizes()
            log.info("Click on Buy Moisturizes.")

            # check any random product name and price value
            product_mois.summer()

            # add to cart product
            result = cart.cart_product()
            if result != None:
                self.assertTrue(True)
            else:
                self.assertFalse(False)

            # cart button click and go on checkout page
            result = checkout.checkout_detail()
            if result != None:
                self.assertTrue(True)
            else:
                self.assertFalse(False)

            # card details
            payment.fill_card_detail()

            # payment done successfully
            time.sleep(10)
            payment.payment_done()

        elif int(curr_temp[:2]) >= 35:
            # click on button of Sunscreens
            get_value.buy_sunscreens()
            log.info("Click on Buy Sunscreens.")

            # assert check any random product name and price value
            product_sun.winter()

            # add to cart product
            result = cart.cart_product()
            if result != None:
                self.assertTrue(True)
            else:
                self.assertFalse(False)

            # cart button click and go on checkout page
            result = checkout.checkout_detail()
            if result != None:
                self.assertTrue(True)
            else:
                self.assertFalse(False)

            # card details
            payment.fill_card_detail()

            # payment done successfully
            time.sleep(10)
            payment.payment_done()
        else:
            log.info(f"Temperature is nor sunscreen neither moisturize.")


if __name__ == '__main__':
    unittest.main()
