'''
This module does end to end actions of MCQ variant
'''

from time import sleep

from generics import base_test
from generics.generics_lib import Generics
from scenes.Classification import Classification
from scenes.LaunchPad import LaunchPad
from scenes.MCQ import MCQ


class TestCase_02_mcq(base_test):
    
    '''
    This contains method that performs end to end actions of MCQ variant
    '''
    def test_01(self):
        
        self.launchPad=LaunchPad(self.altdriver, self.driver)
        self.launchPad.clickMCQ()
        Generics().wait_for_game_load()
        self.mcq=MCQ(self.altdriver,self.driver)
        self.mcq.answer_to_mcq()