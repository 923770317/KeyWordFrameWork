#-*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("\util")
sys.path.append("\configuration")
from util.Constants import Constants
from util.ExcelUtil import ExcelUtil
from util.Log import Log
from configuration.KeyWordsAction import KeyWordsAction
import logging
import logging.config

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)



class TestSuiteByExcel(unittest.TestCase):

    keyWord = ''
    value = ''
    testResult = None

    def setUp(self):
        ExcelUtil.setExcelFile(Constants.path_excelFile,Constants.Sheet_TestSuite)
        logging.config.fileConfig("../log.conf")


    def test_suiteByExcel(self):
        try:
            testCaseCount = ExcelUtil.getRowCount(Constants.Sheet_TestSuite)
            for i in range(1,testCaseCount):
                testCaseId = ExcelUtil.getCellData(Constants.Sheet_TestSuite,i,Constants.Col_TestCaseID)
                testCaseRunFlag = ExcelUtil.getCellData(Constants.Sheet_TestSuite,i,Constants.Col_RunFlag)
                if str(testCaseRunFlag).lower() == "y":
                    Log.startTestCase(testCaseId)
                    TestSuiteByExcel.testResult = True
                    testStep = ExcelUtil.getFirstRowContainsTestCaseId(Constants.Sheet_TestSteps,testCaseId,Constants.Col_TestCaseID)
                    testLastStep = ExcelUtil.getTestCaseLastStepRow(Constants.Sheet_TestSteps,testCaseId,testStep)
                    for j in range(testStep,testLastStep):
                         keyWord = ExcelUtil.getCellData(Constants.Sheet_TestSteps,j,Constants.Col_KeyWordAction)
                         Log.info("从excel读取的关键词为:%s" %(keyWord))
                         value = ExcelUtil.getCellData(Constants.Sheet_TestSteps,j,Constants.Col_ActionValue)
                         Log.info("从excel读取的value为:%s" %(value))
                         locatorExpress = ExcelUtil.getCellData(Constants.Sheet_TestSteps,j,Constants.Col_locatorExpression)
                         Log.info("从excel读取的locator表达式为%s" %(locatorExpress))
                         if hasattr(KeyWordsAction,str(keyWord)):
                            func = getattr(KeyWordsAction,str(keyWord))
                            if(str(keyWord).startswith("assert")):
                                func(self,value)
                            else:
                                func(value,locatorExpress)
                            if KeyWordsAction.testResult == False:
                                #ExcelUtil.setCellData() 在step中写入结果信息
                                TestSuiteByExcel.testResult = False
                                Log.endTestCase(testCaseId)
                                break
                            if KeyWordsAction.testResult == True:
                                pass
                                #ExcelUtil.setCellData() 写step中入结果信息

                         else:
                            print '没有找到相应的方法'
                    if TestSuiteByExcel.testResult == True:
                         #ExcelUtil.setCellData() 在suit中写入结果信息
                         Log.endTestCase(testCaseId)

        except Exception,e:
            AssertionError("执行失败")
            Log.info(str(e))