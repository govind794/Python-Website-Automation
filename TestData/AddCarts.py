'''
Author   : Govind Patidar
DateTime : 11/07/2020 10:00AM
File     : AddCart
'''

from PageObject.add_to_cart_page import AddToCartPageObject


class AddCart():

    def __init__(self, driver):
        '''
        :param driver:
        '''
        self.driver = driver
        self.product = AddToCartPageObject(self.driver)

    def cart_product(self):
        '''
        :return:
        '''
        return self.product.add_cart()
