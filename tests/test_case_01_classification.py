'''
This module does end to end actions of classification variant
'''

from time import sleep


from generics.generics_lib import Generics
from scenes.classification import Classification
from scenes.launch_pad import LaunchPad
from generics.base_test import BaseTest


class Test_Case_01_classification(BaseTest):
    
    '''
    This contains method that performs end to end actions of classification variant
    '''
    def test_01(self):
        
        self.launchPad=LaunchPad(self.altdriver, self.driver)
        self.launchPad.clickClassification()
        Generics().wait_for_game_load()
        self.classification=Classification(self.altdriver,self.driver)
        self.classification.add_draggables_to_bucket()