#-*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("\util")
sys.path.append("\configuration")
from util import Constants
from util import ExcelUtil
from configuration import KeyWordsAction

class TestSuiteByExcel(unittest.TestCase):

    keyWord = ''
    value = ''

    def setUp(self):
        ExcelUtil.ExcelUtil.setExcelFile(Constants.Constants.path_excelFile,Constants.Constants.Sheet_TestSteps)

    def test_suiteByExcel(self):
        try:
            testCaseCount = ExcelUtil.ExcelUtil.getRowCount(Constants.Constants.Sheet_TestSuite)
            for i in range(1,testCaseCount):
                testCaseId = ExcelUtil.ExcelUtil.getCellData(i,Constants.Constants.Col_TestCaseID)
                testCaseRunFlag = ExcelUtil.ExcelUtil.getCellData(i,Constants.Constants.Col_RunFlag)
                if str(testCaseRunFlag).lower() == "y":
                    testStep = ExcelUtil.ExcelUtil.getFirstRowContainsTestCaseId(Constants.Constants.Sheet_TestSteps,testCaseId,Constants.Constants.Col_TestCaseID)
                    testLastStep = ExcelUtil.ExcelUtil.getTestCaseLastStepRow(Constants.Constants.Sheet_TestSteps,testCaseId,testStep)
                    for j in range(testStep - 1,testLastStep):
                         keyWord = ExcelUtil.ExcelUtil.getCellData(j,Constants.Constants.Col_KeyWordAction)
                         value = ExcelUtil.ExcelUtil.getCellData(j,Constants.Constants.Col_ActionValue)
                         if hasattr(KeyWordsAction.KeyWordsAction,str(keyWord)):
                            func = getattr(KeyWordsAction.KeyWordsAction,str(keyWord))
                            if(str(keyWord).startswith("assert")):
                                func(self,value)
                            else:
                                func(value)
                         else:
                            print '没有找到相应的方法'
        except Exception,e:
            print str(e)