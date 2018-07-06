'''
This module contains tasks in Scene Classification
'''

from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from generics import auto_const


class Classification():
    '''
    This class contains methods to perform classification
    '''
    altdriver=None
    driver=None
    
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
        
    def add_draggables_to_bucket(self):
        bucket=self.altdriver.wait_for_element_where_name_contains(auto_const.bucket1)
        draggable=self.altdriver.find_elements(auto_const.dragabble)
        
        act=TouchAction()
        for j in range(auto_const.no_of_levels):
            for i in range(len(draggable)):
                draggable[i].dragToElement(bucket)
                sleep(2)