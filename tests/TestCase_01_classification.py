'''
This module does end to end actions of classification variant
'''

from time import sleep

from generics import base_test
from generics.generics_lib import Generics
from scenes import Classification
from scenes.LaunchPad import LaunchPad


class TestCase_01_classification(base_test):
    
    '''
    This contains method that performs end to end actions of classification variant
    '''
    def test_01(self):
        
        self.launchPad=LaunchPad(self.altdriver, self.driver)
        self.launchPad.clickClassification()
        Generics().wait_for_game_load()
        self.classification=Classification(self.altdriver,self.driver)
        self.classification.add_draggables_to_bucket()