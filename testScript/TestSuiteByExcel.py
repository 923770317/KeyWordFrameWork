#-*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("\util")
sys.path.append("\configuration")
from util import Constants
from util import ExcelUtil
from util import Log
from configuration import KeyWordsAction
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

    def setUp(self):
        ExcelUtil.ExcelUtil.setExcelFile(Constants.Constants.path_excelFile,Constants.Constants.Sheet_TestSuite)
        logging.config.fileConfig("../log.conf")


    def test_suiteByExcel(self):
        try:
            testCaseCount = ExcelUtil.ExcelUtil.getRowCount(Constants.Constants.Sheet_TestSuite)
            for i in range(1,testCaseCount):
                testCaseId = ExcelUtil.ExcelUtil.getCellData(Constants.Constants.Sheet_TestSuite,i,Constants.Constants.Col_TestCaseID)
                testCaseRunFlag = ExcelUtil.ExcelUtil.getCellData(Constants.Constants.Sheet_TestSuite,i,Constants.Constants.Col_RunFlag)
                if str(testCaseRunFlag).lower() == "y":
                    Log.Log.startTestCase(testCaseId)
                    testStep = ExcelUtil.ExcelUtil.getFirstRowContainsTestCaseId(Constants.Constants.Sheet_TestSteps,testCaseId,Constants.Constants.Col_TestCaseID)
                    testLastStep = ExcelUtil.ExcelUtil.getTestCaseLastStepRow(Constants.Constants.Sheet_TestSteps,testCaseId,testStep)
                    for j in range(testStep,testLastStep):
                         keyWord = ExcelUtil.ExcelUtil.getCellData(Constants.Constants.Sheet_TestSteps,j,Constants.Constants.Col_KeyWordAction)
                         Log.Log.info("从excel读取的关键词为:%s" %(keyWord))
                         value = ExcelUtil.ExcelUtil.getCellData(Constants.Constants.Sheet_TestSteps,j,Constants.Constants.Col_ActionValue)
                         Log.Log.info("从excel读取的value为:%s" %(value))
                         if hasattr(KeyWordsAction.KeyWordsAction,str(keyWord)):
                            func = getattr(KeyWordsAction.KeyWordsAction,str(keyWord))
                            if(str(keyWord).startswith("assert")):
                                func(self,value)
                            else:
                                func(value)
                         else:
                            print '没有找到相应的方法'
                         Log.Log.endTestCase(testCaseId)
        except Exception,e:
            AssertionError("执行失败")
            print str(e)