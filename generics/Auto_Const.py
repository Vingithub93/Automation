'''
Created on 03-Jul-2018

@author: Automation
'''


import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

CONTROLLER_PATH = PATH('../data/controller.xlsx')

DRIVER_PATH=PATH('../driver/chromedriver.exe')

ALLURE_PATH=PATH('../reports/allure-report')

REPORT_PATH=PATH('../reports')

APK_PATH=PATH('../game.apk')

IPA_PATH=PATH('../game.ipa')
