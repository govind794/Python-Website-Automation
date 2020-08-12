'''
Author   : Govind Patidar
DateTime : 11/07/2020 11:50AM
File     : Payment
'''

from PageObject.payment_page import PaymentPageObject
from Utility.logs import Logs

log = Logs(log="Payment").getLogs()


class Payment():

    def __init__(self, driver):
        '''
        :param driver:
        '''
        self.driver = driver
        self.payment = PaymentPageObject(self.driver)

    def fill_card_detail(self):
        '''
        # This method use for fill all card details
        :return:
        '''
        self.payment.enter_email()
        log.info("Enter random email id")

        self.payment.enter_card_no()
        log.info("Enter card number")

        self.payment.enter_date()
        log.info("Enter card date")

        self.payment.enter_cvc()
        log.info("Enter card cvc no")

        self.payment.enter_zip_code()
        log.info("Enter zip code no")

        self.payment.pay_now()
        log.info("Payment done")

    def payment_done(self):
        '''
        # This method use for payment done after check string match in payment page
        :return:
        '''
        success = self.payment.payment_success()
        if success == "PAYMENT SUCCESS":
            assert success == "PAYMENT SUCCESS"
            assert True
            log.info("PAYMENT SUCCESS")
        else:
            log.info("PAYMENT Faild")
            assert False

        pay_text = self.payment.payment_text()
        if pay_text:
            assert pay_text == "Your payment was successful. You should receive a follow-up call from our sales team."
            assert True
        else:
            assert False
