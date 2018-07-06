'''
Created on 06-Jul-2018

@author: Automation
'''
from generics.BaseTest import BaseTest
from scenes.LaunchPad import LaunchPad
import time

class TestCase_02_LaunchPad(BaseTest):
    '''
    classdocs
    '''
    
    def test(self):
        self.launchPad=LaunchPad(self.altdriver, self.driver)
        
        self.launchPad.clickMCQ()
        time.sleep(5)