'''
Author   : Govind Patidar
DateTime : 10/07/2020 11:30AM
File     : BrowserLoad
'''

import os.path
from configparser import ConfigParser
from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

from Utility.logs import Logs

log = Logs(log="BrowserLoad").getLogs()


class BrowserLoad(object):
    # Set the absolute path for drivers
    dir = os.path.dirname(os.path.abspath(''))

    # Get all browser
    chrome_driver_path = dir + "/Driver/chromedriver"
    firefox_driver_path = dir + "/Driver/geckodriver"
    ie_driver_path = dir + "/Driver/geckodriver"
    # Safari_driver_path = dir + "/Driver/safaridriver"
    edge_driver_path = dir + "/Driver/msedgedriver"

    # Define the constructor
    def __init__(self, driver):
        '''
        :param driver:
        '''
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def browserOpen(self, driver):
        '''
        # Which browser do you want to test? He has to go to the config.ini file and uncomment browser name.
        :param driver:
        :return:
        '''
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('')) + "/Config/config.ini"
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        log.info(f"You had select {browser} browser.")
        url = config.get("testUrl", "URL")
        log.info(f"The test url is: {url}")

        # check browser name right or wrong
        print("--------Open browser--------")
        if browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            log.info("Start chrome browser.")
        elif browser == "Firefox":
            driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
            log.info("Start Firefox browser.")
        elif browser == "IE":
            driver = webdriver.Ie(executable_path=self.ie_driver_path)
            log.info("Start IE browser.")
        elif browser == "Safari":
            driver = webdriver.Safari(executable_path="/use/local/bin/safaridriver")
            log.info("Start safari browser.")
        elif browser == "Edge":
            # driver = webdriver.Edge(executable_path=self.edge_driver_path)
            # edge_options = EdgeOptions()
            # edge_options.use_chromium = True  # if we miss this line, we can't make Edge headless
            # # A little different from Chrome cause we don't need two lines before 'headless' and 'disable-gpu'
            # edge_options.add_argument('headless')
            # edge_options.add_argument('disable-gpu')
            #
            # driver = Edge(executable_path=self.edge_driver_path, options=edge_options)
            driver = Edge(executable_path=self.edge_driver_path)
            log.info("Start Edge browser.")

        driver.get(url)
        log.info(f"Open url: {url}")
        driver.maximize_window()
        log.info("Maximize the current window.")
        driver.implicitly_wait(10)
        log.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        '''
        :return:
        '''
        log.info("Now, Close and quit the browser.")
        self.driver.quit()
