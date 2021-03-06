'''
Created on 04-Jul-2018

@author: Automation
'''



import os
import subprocess

from selenium.webdriver.chrome.webdriver import WebDriver

from generics import excel_library, setup
from generics.testdroid import Android, iOS
from generics.testdroid import webdriver


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def execution():    
    executionEnvi=excel_library.get_Cellvalue('../data/controller.xlsx', 'execution_controller', 0, 1)
    executionPlatform=excel_library.get_Cellvalue('../data/controller.xlsx', 'execution_controller', 1, 1)
    
    testcases=None
    value=excel_library.get_Cellvalue('../data/controller.xlsx', 'test_case_controller', 1, 1)
    print value
    if value=='yes':
        testcases='complete'
    else:
        testcases=[]
        check1=excel_library.get_columnValues('../data/controller.xlsx', 'test_case_controller', 0)
        status=excel_library.get_columnValues('../data/controller.xlsx', 'test_case_controller', 1)
        
        for i in range(len(check1)):
            if status[i]=='yes':
                testcases.append(check1[i])
            
    print 'Added '+str(testcases)+' testcases'
    
    if(executionEnvi=='Testdroid Cloud'):
        if(executionPlatform=='Android'):
            #shutil.move('../android.sh', '../run-tests.sh')
            os.rename('../android.sh', '../run-tests.sh')
            replaceValue=None
            if testcases=='complete':
                with open('../run-tests.sh', 'r') as file :
                    filedata = file.read()

                # Replace the target string
                filedata = filedata.replace('replace', 'TEST=${TEST:=""}')

                # Write the file out again
                with open('../run-tests.sh', 'w') as file:
                    file.write(filedata)
            else:       
                replaceValue='TEST=${TEST:="'
            
            
                for i in range(len(testcases)):
                    replaceValue=replaceValue+'tests/'+testcases[i]+'.py '
                    
                replaceValue=replaceValue+'"}'
            
            
                print 'file create complete 2'
                with open('../run-tests.sh', 'r') as file :
                    filedata = file.read()

                # Replace the target string
                filedata = filedata.replace('replace', replaceValue)

                # Write the file out again
                with open('../run-tests.sh', 'w') as file:
                    file.write(filedata)
            os.chdir(PATH('../'))
            subprocess.call('zip -r tests.zip *')
            os.chdir('generics')
            
            with open('../run-tests.sh', 'r') as file :
                filedata = file.read()

            # Replace the target string
            filedata = filedata.replace(replaceValue, 'replace')

            # Write the file out again
            with open('../run-tests.sh', 'w') as file:
                file.write(filedata)
            os.rename('../run-tests.sh', '../android.sh')
            
            device_group=excel_library.get_Cellvalue('../data/controller.xlsx', 'testdroid', 0, 1);
            test_runName=excel_library.get_Cellvalue('../data/controller.xlsx', 'testdroid', 1, 1);
            print device_group
            print test_runName
            Android(device_group, test_runName)
            
        elif(executionPlatform=='iOS'):
            os.rename('../ios.sh', '../run-tests.sh')
            if testcases=='complete':
                with open('../run-tests.sh', 'r') as file :
                    filedata = file.read()

                # Replace the target string
                filedata = filedata.replace('replace', 'TEST=${TEST:=""}')

                # Write the file out again
                with open('../run-tests.sh', 'w') as file:
                    file.write(filedata)
            else:       
                replaceValue='TEST=${TEST:="'
            
            
                for i in range(len(testcases)):
                    replaceValue=replaceValue+'tests/'+testcases[i]+'.py '
                    
                replaceValue=replaceValue+'"}'
            
            
                print 'file create complete 2'
                with open('../run-tests.sh', 'r') as file :
                    filedata = file.read()

                # Replace the target string
                filedata = filedata.replace('replace', replaceValue)

                # Write the file out again
                with open('../run-tests.sh', 'w') as file:
                    file.write(filedata)
            os.chdir(PATH('../'))
            subprocess.call('zip -r tests.zip *')
            os.chdir('generics')
            
            with open('../run-tests.sh', 'r') as file :
                filedata = file.read()

            # Replace the target string
            filedata = filedata.replace(replaceValue, 'replace')

            # Write the file out again
            with open('../run-tests.sh', 'w') as file:
                file.write(filedata)
            os.rename('../run-tests.sh', '../ios.sh')
            
            device_group=excel_library.get_Cellvalue('../data/controller.xlsx', 'testdroid', 1, 0);
            test_runName=excel_library.get_Cellvalue('../data/controller.xlsx', 'testdroid', 1, 1);
            print device_group
            print test_runName
            iOS(device_group, test_runName)
            
    elif (executionEnvi=='Local Devices'):
        subprocess.call('adb devices')
        subprocess.call('adb forward tcp:13001 tcp:13000')
        setup.main()
        
execution()