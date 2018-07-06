'''
This module contains generic methods
'''
from time import sleep

class Generics(object):
    
    def scroll(self, driver,start_xvalue, end_xvalue, start_yvalue, end_yvalue):
        
        dSize=driver.get_window_size()
        start_x=dSize['width']*start_xvalue
        end_x=dSize['width']*end_xvalue
        start_y=dSize['height']*start_yvalue
        end_y=dSize['height']*end_yvalue
        driver.swipe(start_x, start_y, end_x, end_y)
        
    def wait_for_game_load(self):
        sleep(4)
        
    def think_time(self):
        sleep(2)