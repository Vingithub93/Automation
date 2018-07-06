'''
This module does end to end actions of MCQ variant
'''

from time import sleep


from generics.generics_lib import Generics
from scenes.classification import Classification
from scenes.launch_pad import LaunchPad
from scenes.mcq import MCQ
from generics.base_test import BaseTest


class Test_Case_02_mcq(BaseTest):
    
    '''
    This contains method that performs end to end actions of MCQ variant
    '''
    def test_01(self):
        
        self.launchPad=LaunchPad(self.altdriver, self.driver)
        self.launchPad.clickMCQ()
        Generics().wait_for_game_load()
        self.mcq=MCQ(self.altdriver,self.driver)
        self.mcq.answer_to_mcq()