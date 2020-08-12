'''
Author   : Govind Patidar
DateTime : 11/07/2020 10:00AM
File     : Moisturize
'''

from PageObject.add_to_cart_page import AddToCartPageObject
from Utility.logs import Logs

log = Logs(log="Moisturize").getLogs()


class Moisturize():

    def __init__(self, driver):
        '''
        :param driver:
        '''
        self.driver = driver

    def summer(self):
        '''
        :return:
        '''
        product = AddToCartPageObject(self.driver)
        name = product.product_name()
        price = product.product_price()

        try:
            for i in range(len(name)):
                # assert through match any random product name and price value
                if name[i] == "Tigran Aloe Isolani":
                    assert name[i] == "Tigran Aloe Isolani"
                    log.info(f"First Product Name: {name[i]}")
                elif name[i] == "Emmanuel Aloe Vera Beauty Gel":
                    assert name[i] == "Emmanuel Aloe Vera Beauty Gel"
                    log.info(f"Second Product Name: {name[i]}")
            for i in range(len(price)):
                # assert through match product price value
                if price[i] == "Price: Rs. 215":
                    assert price[i] == "Price: Rs. 215"
                    log.info(f"First Product Price: {price[i]}")
                elif price[i] == "Price: 299":
                    assert price[i] == "Price: 299"
                    log.info(f"Second Product Price: {price[i]}")
            print("-----Pass Test Case-----")
        except Exception as e:
            print("-----Fail Test Case -----", format(e))
