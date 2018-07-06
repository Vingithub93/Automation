'''
Created on 04-Jul-2018

@author: Automation
'''

class LaunchPad(object):
    '''
    classdocs
    '''
    
    altdriver=None
    driver=None
    
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
        
    def clickClassification(self):
        self.altdriver.wait_for_current_scene_to_be('LaunchPad')
        self.altdriver.wait_for_element('Button').tap()
        self.altdriver.wait_for_current_scene_to_be('classification')
        
    def clickMCQ(self):
        self.altdriver.wait_for_current_scene_to_be('LaunchPad')
        self.altdriver.wait_for_element('MCQ').tap()
        self.altdriver.wait_for_current_scene_to_be('MCQ')
    