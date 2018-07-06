'''
Created on 06-Jul-2018

@author: Automation
'''
from scenes.LaunchPad import LaunchPad
from generics.BaseTest import BaseTest
import time

class TestCase_01_LaunchPad(BaseTest):
    '''
    classdocs
    '''
    
    def test_01(self):
        
        self.launchPad=LaunchPad(self.altdriver, self.driver)
        self.launchPad.clickClassification()
        
        