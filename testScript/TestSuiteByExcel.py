#-*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("\util")
sys.path.append("\configuration")
from util import Constants
from util import ExcelUtil
from configuration import KeyWordsAction
import logging
import logging.config

class TestSuiteByExcel(unittest.TestCase):

    keyWord = ''
    value = ''

    def setUp(self):
        ExcelUtil.ExcelUtil.setExcelFile(Constants.Constants.path_excelFile,Constants.Constants.Sheet_TestSuite)
        logging.config.fileConfig("..\logging.conf")
        logger = logging.getLogger()

    def test_suiteByExcel(self):
        try:
            testCaseCount = ExcelUtil.ExcelUtil.getRowCount(Constants.Constants.Sheet_TestSuite)
            for i in range(1,testCaseCount):
                testCaseId = ExcelUtil.ExcelUtil.getCellData(Constants.Constants.Sheet_TestSuite,i,Constants.Constants.Col_TestCaseID)
                testCaseRunFlag = ExcelUtil.ExcelUtil.getCellData(Constants.Constants.Sheet_TestSuite,i,Constants.Constants.Col_RunFlag)
                if str(testCaseRunFlag).lower() == "y":
                    KeyWordsAction.logger.startTestCase(testCaseId)
                    testStep = ExcelUtil.ExcelUtil.getFirstRowContainsTestCaseId(Constants.Constants.Sheet_TestSteps,testCaseId,Constants.Constants.Col_TestCaseID)
                    testLastStep = ExcelUtil.ExcelUtil.getTestCaseLastStepRow(Constants.Constants.Sheet_TestSteps,testCaseId,testStep)
                    for j in range(testStep,testLastStep):
                         keyWord = ExcelUtil.ExcelUtil.getCellData(Constants.Constants.Sheet_TestSteps,j,Constants.Constants.Col_KeyWordAction)
                         KeyWordsAction.logger.info("从excel读取的关键词为:" ,keyWord)
                         value = ExcelUtil.ExcelUtil.getCellData(Constants.Constants.Sheet_TestSteps,j,Constants.Constants.Col_ActionValue)
                         KeyWordsAction.logger.info("从excel读取的value为:" ,value)
                         if hasattr(KeyWordsAction.KeyWordsAction,str(keyWord)):
                            func = getattr(KeyWordsAction.KeyWordsAction,str(keyWord))
                            if(str(keyWord).startswith("assert")):
                                func(self,value)
                            else:
                                func(value)
                         else:
                            print '没有找到相应的方法'
                         KeyWordsAction.logger.endTestCase(testCaseId)
        except Exception,e:
            AssertionError("执行失败")
            print str(e)