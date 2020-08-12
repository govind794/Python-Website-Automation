'''
Author   : Govind Patidar
DateTime : 11/07/2020 11:40AM
File     : Checkout
'''

import time
from PageObject.checkout_page import CheckoutPageObject
from Utility.logs import Logs

log = Logs(log="Checkout").getLogs()


class Checkout():

    def __init__(self, driver):
        '''
        :param driver:
        '''
        self.driver = driver
        self.checkout = CheckoutPageObject(self.driver)

    def checkout_detail(self):
        '''
        :return:
        '''
        self.checkout.cart_btn()
        log.info("Click cart button.")
        # checkout page details
        amount = self.checkout.checkout_details()
        log.info(f"Checkout page added product total amount: {amount}")

        total_amount = self.checkout.total_amount()
        # match amount and total amount value
        log.info(total_amount)

        if str(amount) == total_amount[14:]:
            assert str(amount) in total_amount
            assert True
        else:
            assert False

        # click on pay with cart button
        self.checkout.pay()
        time.sleep(10)
        log.info("Click pay with cart button.")
