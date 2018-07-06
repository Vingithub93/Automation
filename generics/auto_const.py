'''
This module is used to store testdata
'''
import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

#testdata
dragabble='Sprite'
bucket1='Box'
no_of_levels=2
question1='mcq_fourdigittothreedigit_stage_001(Clone)'
ans1='Option 1'
question2='mcq_fourdigittothreedigit_stage_002(Clone)'
ans2='Option 1'
question3='mcq_fourdigittothreedigit_stage_003(Clone)'
ans3='Option 1'
#paths
CONTROLLER_PATH = PATH('../data/controller.xlsx')
DRIVER_PATH=PATH('../driver/chromedriver.exe')
ALLURE_PATH=PATH('../reports/allure-report')
REPORT_PATH=PATH('../reports')
APK_PATH=PATH('../game.apk')
IPA_PATH=PATH('../game.ipa')
