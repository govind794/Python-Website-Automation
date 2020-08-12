'''
Author   : Govind Patidar
DateTime : 10/07/2020 03:30PM
File     : AddToCartPageObject
'''

from selenium.webdriver.common.by import By
from PageLocator.all_page_locators import AllPageLocators


class AddToCartPageObject():

    def __init__(self, driver):
        '''
        :param driver:
        '''
        self.driver = driver
        self.locator = AllPageLocators

    def product_name(self):
        productName = []
        for r in range(2, 4):
            for c in range(1, 4):
                name = self.driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div[' + str(r) + ']/div[' + str(c) + ']/p[1]').text
                productName.append(name)
        return productName

    def product_price(self):
        productPrice = []
        for r in range(2, 4):
            for c in range(1, 4):
                price = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[' + str(r) + ']/div[' + str(c) + ']/p[2]').text
                productPrice.append(price)
        return productPrice

    def add_cart(self):
        # for r in range(2, 4):
        #     for c in range(1, 4):
        #         self.driver.find_element(By.XPATH,
        #                                  '/html/body/div[1]/div[' + str(r) + ']/div[' + str(r) + ']/button').click()

        for r in range(1, 4):
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[' + str(r) + ']/button').click()
        for r in range(1, 4):
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[' + str(r) + ']/button').click()
