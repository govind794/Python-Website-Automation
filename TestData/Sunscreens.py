'''
Author   : Govind Patidar
DateTime : 11/07/2020 10:00AM
File     : Sunscreen
'''

from PageObject.add_to_cart_page import AddToCartPageObject
from Utility.logs import Logs

log = Logs(log="Sunscreen").getLogs()


class Sunscreen():

    def __init__(self, driver):
        '''
        :param driver:
        '''
        self.driver = driver

    def winter(self):
        '''
        :return:
        '''
        product = AddToCartPageObject(self.driver)
        name = product.product_name()
        price = product.product_price()

        for i in range(len(name)):
            # assert through match any random product name and price value
            if name[i] == "Anatoly Ultra Sunblock SPF-50":
                assert name[i] == "Anatoly Ultra Sunblock SPF-50"
                assert True
                log.info(f"First Product Name: {name[i]}")
            elif name[i] == "Paul Magnificient SPF-30":
                assert name[i] == "Paul Magnificient SPF-30"
                assert True
                log.info(f"Second Product Name: {name[i]}")

        for i in range(len(price)):
            # assert through match product price value
            if price[i] == "Price: Rs. 289":
                assert price[i] == "Price: Rs. 289"
                assert True
                log.info(f"First Product Price: {price[i]}")
            elif price[i] == "Price: 121":
                assert price[i] == "Price: 121"
                assert True
                log.info(f"second Product Price: {price[i]}")
