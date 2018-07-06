
'''
This module used for setting up initial and final actions
'''

import os

from altunityrunner import AltrunUnityDriver
from appium import webdriver
import pytest

from generics import excel_library, auto_const


class BaseTest():
    
    altdriver = None
    driver=None
    eledriver=  None
    text= None
    platform = None
    
    @classmethod
    def setup_class(self):
        """
        This method is used to setup desired capabilities and launch app

        """
        self.platform=excel_library.get_Cellvalue(auto_const.CONTROLLER_PATH, 'execution_controller', 1, 1)
        print "platform name = "+self.platform
        
        self.desired_caps = {}
        
        if (self.platform == "Android"):
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['deviceName'] = 'device'
            self.desired_caps['app'] = auto_const.APK_PATH
            self.desired_caps['newCommandTimeout'] = 400
        else: 
            self.desired_caps['platformName'] = 'iOS'
            self.desired_caps['deviceName'] = 'iPhone8'
            self.desired_caps['automationName'] = 'XCUITest'
            self.desired_caps['app'] = auto_const.IPA_PATH

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.altdriver = AltrunUnityDriver(self.driver, self.platform)


    @classmethod
    def teardown_class(self):
        """
        This method is used to close app and open report

        """
        self.altdriver.stop()
        self.driver.quit()
        if excel_library.get_Cellvalue(auto_const.CONTROLLER_PATH, 'execution_controller', 0, 1)=='Local Devices':
            os.chdir(auto_const.REPORT_PATH)
            os.startfile('Report.bat')
      
if __name__ == '__main__':
    pytest.main()
