'''
Author   : Govind Patidar
DateTime : 10/07/2020 11:30AM
File     : Logs
'''

import logging
import os.path
import time


class Logs(object):
    def __init__(self, log):
        '''
        # Level set of the logger funtion
        :param log:
        '''
        self.log = logging.getLogger(log)
        self.log.setLevel(logging.DEBUG)

        # set the datetime for log file
        setTime = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
        # set the path of log file
        path = os.path.dirname(os.path.abspath('.')) + '/Logs/'
        # set time log file extension formate
        log_file = path + setTime + '.log'

        hendler = logging.FileHandler(log_file, encoding="utf-8")
        hendler.setLevel(logging.INFO)

        self.log.addHandler(hendler)

    def getLogs(self):
        '''
        # return log file
        :return:
        '''
        return self.log
