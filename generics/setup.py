'''
Created on 03-Jul-2018

@author: Automation
'''

import os
import xlrd

from generics import auto_const


def main():
    f=open("../test_run.bat", "w+")
    check=None
    status=None
        
    book=xlrd.open_workbook(auto_const.CONTROLLER_PATH)
    sheet=book.sheet_by_name('test_case_controller')
        
    value=sheet.cell_value(1,1)
        
    print value
    if value=='yes':
        check='complete'
    else:
        check=[]
        check1=sheet.col_values(0)
        status=sheet.col_values(1)
            
        for i in range(len(check1)):
            if status[i]=='yes':
                check.append(check1[i])
        
    if check=='complete':
        f.write('pytest --alluredir "%CD%"\\reports\\allure-report')
        f.close()
        print 'file create complete 1'
    else:
        f.write('pytest ')
        for i in range(len(check)):
            f.write('tests/'+check[i]+'.py ')
        f.write('--alluredir "%CD%"\\reports\\allure-report')
        f.close()
        print 'file create complete 2'
            
    os.chdir(auto_const.PATH('../'))
    os.startfile("test_run.bat")
    print 'file execution started'