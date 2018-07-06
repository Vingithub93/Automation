
'''
Created on 03-Jul-2018

@author: Automation
'''

import os

from altunityrunner import AltrunUnityDriver
from appium import webdriver
import pytest
from generics import ExcelLibrary, Auto_Const

class BaseTest():
    '''
    classdocs
    '''


    altdriver = None
    driver=None
    eledriver=  None
    text= None
    platform = None
    
    @classmethod
    def setup_class(self):
        
        self.platform=ExcelLibrary.get_Cellvalue(Auto_Const.CONTROLLER_PATH, 'execution_controller', 1, 1)
        print "platform name = "+self.platform
        
        self.desired_caps = {}
        
        if (self.platform == "Android"):
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['deviceName'] = 'device'
            self.desired_caps['app'] = Auto_Const.APK_PATH
            self.desired_caps['newCommandTimeout'] = 400
        else: 
            self.desired_caps['platformName'] = 'iOS'
            self.desired_caps['deviceName'] = 'iPhone8'
            self.desired_caps['automationName'] = 'XCUITest'
            self.desired_caps['app'] = Auto_Const.IPA_PATH

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.altdriver = AltrunUnityDriver(self.driver, self.platform)


    @classmethod
    def teardown_class(self):
        self.altdriver.stop()
        self.driver.quit()
        if ExcelLibrary.get_Cellvalue(Auto_Const.CONTROLLER_PATH, 'execution_controller', 0, 1)=='Local Devices':
            os.chdir(Auto_Const.REPORT_PATH)
            os.startfile('Report.bat')
      
if __name__ == '__main__':
    pytest.main()
