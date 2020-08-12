'''
Author   : Govind Patidar
DateTime : 10/07/2020 11:30AM
File     : HomePage
'''

import unittest
from Utility.browser_load import BrowserLoad
from PageObject.home_page import HomePageObject
from Utility.logs import Logs

log = Logs(log="Homepage").getLogs()


class HomePage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        '''
        #Load browser
        :return:
        '''
        print("------- Start Test Case--------")
        cls.browser = BrowserLoad(cls)
        cls.driver = cls.browser.browserOpen(cls)

    @classmethod
    def tearDownClass(cls):
        '''
        :return:
        '''
        print("--------Complate Test Case--------")
        cls.driver.quit()

    def test_HomePage(self):
        '''
        :return:
        '''
        # Home page object class extend
        page = HomePageObject(self.driver)

        # get string text current temp
        text_curr_temp = page.text_curr_temp()

        # get temp value
        curr_temp = page.curr_temp()
        try:
            # assert through match title string value
            assert self.driver.title == "Current Temperature"
            log.info(f"Title: {self.driver.title}")

            # assert through match current temp text value
            assert text_curr_temp == "Current temperature"
            log.info(f"Text current Temp: {text_curr_temp}")

            # log temp value
            log.info(f"Get current Temp: {curr_temp}")
            print("-----Pass Test Case-----")
        except Exception as e:
            print("-----Fail Test Case -----", format(e))

    def test_Based_On_Temp(self):
        '''
        :return:
        '''
        get_value = HomePageObject(self.driver)

        # get temperature value
        curr_temp = get_value.curr_temp()

        # read Instructions of moisturizes
        moisturize = get_value.moisturizes()

        # read Instructions of sunscreens
        sunscreen = get_value.sunscreens()

        # check condition on Temperature of sunscreens and moisturizes
        if int(curr_temp[:2]) <= 18:
            # assert through match instructions of moisturize
            assert moisturize == "Don't let cold weather ruin your skin. Use your favourite moisturizer and keep your skin stay young."
            log.info(f"Moisturize: {moisturize}")
        elif int(curr_temp[:2]) >= 35:
            # assert through match instructions of sunscreen
            assert sunscreen == "Treat your skin right. Don't leave your home without your favorite sunscreen. Say goodbye to sunburns."
            log.info(f"Sunscreen: {sunscreen}")
        else:
            log.info(f"Temperature is nor sunscreen neither moisturize.")


if __name__ == '__main__':
    unittest.main()
