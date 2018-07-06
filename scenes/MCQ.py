'''
This module contains tasks in MCQ scene
'''
from time import sleep

from generics import auto_const
import generics


class MCQ(object):
    '''
    This class contains methods to perform mcq actions
    '''
    altdriver=None
    driver=None
    
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
        
    def answer_to_mcq(self):
        self.altdriver.wait_for_element(auto_const.question1)
        generics().think_time()
        self.altdriver.find_element(auto_const.ans1).tap()
        
        self.altdriver.wait_for_element(auto_const.question2)
        generics().think_time()
        self.altdriver.find_element(auto_const.ans2).tap()
        
        self.altdriver.wait_for_element(auto_const.question3)
        generics().think_time()
        self.altdriver.find_element(auto_const.ans3).tap()