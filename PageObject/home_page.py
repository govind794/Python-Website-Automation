'''
Author   : Govind Patidar
DateTime : 10/07/2020 11:30AM
File     : HomePageObject
'''

from selenium.webdriver.common.by import By
from PageLocator.all_page_locators import AllPageLocators


class HomePageObject():

    def __init__(self, driver):
        '''
        :param driver:
        '''
        self.driver = driver
        self.locator = AllPageLocators

    def text_curr_temp(self):
        return self.driver.find_element(By.XPATH, self.locator.text_curr_temp).text

    def curr_temp(self):
        return self.driver.find_element(By.ID, self.locator.curr_temp).text

    def moisturizes(self):
        return self.driver.find_element(By.XPATH, self.locator.moisturizes).text

    def buy_moisturizes(self):
        return self.driver.find_element(By.XPATH, self.locator.buy_moisturizes).click()

    def sunscreens(self):
        return self.driver.find_element(By.XPATH, self.locator.sunscreens).text

    def buy_sunscreens(self):
        return self.driver.find_element(By.XPATH, self.locator.buy_sunscreens).click()
