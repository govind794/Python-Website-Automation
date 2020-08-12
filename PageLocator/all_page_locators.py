'''
Author   : Govind Patidar
DateTime : 10/07/2020 11:30AM
File     : AllPageLocators
'''


class AllPageLocators():

    def __init__(self, driver):
        '''
        :param driver:
        '''
        self.driver = driver

    '''Home page locator'''

    # get XPATH current temperature text
    text_curr_temp = '/html/body/div/div[1]/h2'
    # get ID current temperature value
    curr_temp = "temperature"
    # get XPATH moisturizes text
    moisturizes = '/html/body/div/div[3]/div[1]/p'
    # get XPATH buy moisturizes
    buy_moisturizes = '/html/body/div/div[3]/div[1]/a/button'
    # get XPATH sunscreens text
    sunscreens = '/html/body/div/div[3]/div[2]/p'
    # get XPATH buy sunscreens
    buy_sunscreens = '/html/body/div/div[3]/div[2]/a/button'

    '''Checkout page locator'''

    # get ID in add to cart items
    add_cart = 'cart'

    # get ID total amount
    total_amount = 'total'

    # get XPATH pay with cart button
    pay = '/html/body/div[1]/div[3]/form/button/span'

    '''Payment page'''

    # get XPATH payment page
    email = '//input[@type="email"]'
    cardNo = '//input[@type="tel"]'
    date = '//input[@placeholder="MM / YY"]'
    cvc = '//input[@placeholder="CVC"]'
    zip = '//input[@placeholder="ZIP Code"]'
    paynow = '//*[@id="container"]/section/span[2]/div/div/main/form/nav/div/div/div/button'

    '''Payment done'''
    pay_success = '/html/body/div/div[1]/h2'
    pay_text = '/html/body/div/div[2]/p'
