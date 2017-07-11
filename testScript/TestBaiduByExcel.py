#-*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("\util")
sys.path.append("\configuration")
from util import ExcelUtil
from configuration import KeyWordsAction
from util import Constants

class TestBaiduByExcel(unittest.TestCase):
    keyWord = ''
    value = ''


    def setUp(self):
        ExcelUtil.ExcelUtil.setExcelFile(Constants.Constants.path_excelFile,Constants.Constants.Sheet_TestSteps)

    def tearDown(self):
        pass

    def test_baiduByExcel(self):
        for i in range(1,ExcelUtil.ExcelUtil.getLastRowNum()):
            keyWord = ExcelUtil.ExcelUtil.getCellData(Constants.Constants.Sheet_TestSteps,i,Constants.Constants.Col_KeyWordAction)
            value = ExcelUtil.ExcelUtil.getCellData(Constants.Constants.Sheet_TestSteps,i,Constants.Constants.Col_ActionValue)

            if hasattr(KeyWordsAction.KeyWordsAction,str(keyWord)):
                func = getattr(KeyWordsAction.KeyWordsAction,str(keyWord))
                if(str(keyWord).startswith("assert")):
                    func(self,value)
                else:
                    func(value)
            else:
                print '没有找到相应的方法'

if __name__ =="__main__":
    unittest.main()
