'''
Author   : Govind Patidar
DateTime : 11/07/2020 07:00AM
File     : CheckoutPageObject
'''

from selenium.webdriver.common.by import By
from PageLocator.all_page_locators import AllPageLocators


class CheckoutPageObject():

    def __init__(self, driver):
        self.driver = driver
        self.locator = AllPageLocators

    def cart_btn(self):
        return self.driver.find_element(By.ID, self.locator.add_cart).click()

    def checkout_details(self):
        rows = self.driver.find_elements(By.XPATH,
                                         '/html/body/div[1]/div[2]/table/tbody/tr')  # count no of rows
        sum = 0
        for r in range(1, len(rows) + 1):  # iterate no of rows in amount clo on checkout page
            value = self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div[2]/table/tbody/tr[' + str(r) + ']/td[2]').text
            sum += int(value)  # sum of all product price
        return sum

    def total_amount(self):
        return self.driver.find_element(By.ID, self.locator.total_amount).text

    def pay(self):
        return self.driver.find_element(By.XPATH, self.locator.pay).click()
