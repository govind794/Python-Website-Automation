'''
Author   : Govind Patidar
DateTime : 10/07/2020 11:30AM
File     : PaymentPage
'''

from selenium.webdriver.common.by import By
from PageLocator.all_page_locators import AllPageLocators
from configparser import ConfigParser

import os


class PaymentPageObject():

    def __init__(self, driver):
        '''
        :param driver:
        '''
        self.driver = driver
        self.locator = AllPageLocators

        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('')) + "/Config/config.ini"
        config.read(file_path)

        self.email = config.get("cardDetails", "email")
        self.cardNo = config.get("cardDetails", "cardNo")
        self.date = config.get("cardDetails", "date")
        self.cvc = config.get("cardDetails", "cvc")
        self.zip_code = config.get("cardDetails", "zip_code")

    def enter_email(self):
        self.driver.switch_to_frame(
            frame_reference=self.driver.find_element(By.XPATH, '//iframe[@name="stripe_checkout_app"]'))
        self.driver.set_page_load_timeout(5)
        return self.driver.find_element(By.XPATH, self.locator.email).send_keys(self.email)

    def enter_card_no(self):
        return self.driver.find_element(By.XPATH, self.locator.cardNo).send_keys(self.cardNo)

    def enter_date(self):
        return self.driver.find_element(By.XPATH, self.locator.date).send_keys(self.date)

    def enter_cvc(self):
        return self.driver.find_element(By.XPATH, self.locator.cvc).send_keys(self.cvc)

    def enter_zip_code(self):
        return self.driver.find_element(By.XPATH, self.locator.zip).send_keys(self.zip_code)

    def pay_now(self):
        return self.driver.find_element(By.XPATH, self.locator.paynow).click()

    def payment_success(self):
        self.driver.set_page_load_timeout(5)
        return self.driver.find_element(By.XPATH, self.locator.pay_success).text

    def payment_text(self):
        return self.driver.find_element(By.XPATH, self.locator.pay_text).text
