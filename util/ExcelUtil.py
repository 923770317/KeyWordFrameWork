 #-*- coding: utf-8 -*-
import Constants
import xlrd
import xlwt
from xlutils.copy import copy


class ExcelUtil():
    excelSheet = None
    excelBook = None
    Cell = None
    Row = None
    curRowNo = 1

    @staticmethod
    def setExcelFile(path,sheetName):
        try:
            ExcelUtil.excelSheet = xlrd.open_workbook(unicode(path,"utf-8"))
            ExcelUtil.excelBook = ExcelUtil.excelSheet.sheet_by_name(sheetName)
        except Exception,e:
            print str(e)


    @staticmethod
    def getCellData(rowNum,colNum):
        try:
            cellData = ExcelUtil.excelBook.cell(rowNum,colNum).value
            return cellData
        except Exception,e:
            print str(e)


    @staticmethod
    def getLastRowNum():
        try:
            return ExcelUtil.excelBook.nrows
        except Exception,e:
            print str(e)


    @staticmethod
    def setCellData(rowNum,colNum,result,path):
        try:
            oldWb = xlrd.open_workbook(path, formatting_info=True)
            newWb = copy(oldWb)
            nweWs = newWb.get_sheet(0)
            nweWs.write(rowNum,colNum,unicode(result))
            newWb.save(path)

        except Exception,e:
            print str(e)


    @staticmethod
    def gonext():
       r = []
       while ExcelUtil.hasNext():
           s = {}
           col = ExcelUtil.excelBook.row_values(ExcelUtil.curRowNo)
           i = ExcelUtil.excelBook.ncols
           for x in range(i):
               s[ExcelUtil.excelBook.row_values(0)[x]] = col[x]
           r.append(s)
           ExcelUtil.curRowNo += 1
       return r


    @staticmethod
    def getValue():
        r = []
        try:
            for x in range(1,ExcelUtil.excelBook.nrows):
                r.append(ExcelUtil.excelBook.row_values(x))
            return r
        except Exception,e:
            print str(e)


    @staticmethod
    def hasNext():
        if ExcelUtil.excelBook.nrows == 0 or ExcelUtil.excelBook.nrows <= ExcelUtil.curRowNo:
            return False
        else:
            return True


    #获取指定sheet 中的总行数
    @staticmethod
    def getRowCount(sheetName):
        try:
            number = ExcelUtil.getLastRowNum()
            return number
        except Exception,e:
            print str(e)


    #在指定sheet中，获取第一次包含指定测试用例序号文字的行号
    @staticmethod
    def getFirstRowContainsTestCaseId(sheentName,testCaseName,colNum):
        try:
            flag = False
            rowNum = ExcelUtil.getRowCount(sheentName)
            for i in range(1,rowNum):
                if str(ExcelUtil.getCellData(i,colNum)).lower() == testCaseName:
                    flag = True
                    return i
            if(flag == False):
                raise Exception("么有")
        except Exception,e:
            print str(e)


    #获取指定Sheet中某个测试用例步骤的个数
    @staticmethod
    def getTestCaseLastStepRow(sheetName,testCaseId,testCaseStartRowNum):
        try:
            rowNum = ExcelUtil.getRowCount(sheetName)
            for i in range(testCaseStartRowNum,rowNum):
                if not str(ExcelUtil.getCellData(i,Constants.Constants.Col_TestCaseID)).lower() == testCaseId :
                    return i
            #如果是 最后一行结束
            return rowNum + 1
        except Exception,e:
            print str(e)


if __name__ == "__main__":
    # codedetect = chardet.detect("百度测试数据.xls")["encoding"]
    # print codedetect
    # ustring = unicode("百度测试数据.xls", codedetect)
    ExcelUtil.setExcelFile(Constants.Constants.path_excelFile,Constants.Constants.Sheet_TestSteps)
    # # ExcelUtil.setCellData(5,1,'sema')
    # # print ExcelUtil.excelBook.row_values(0)
    # # ExcelUtil.gonext()
    print ExcelUtil.getFirstRowContainsTestCaseId("testsuite","baidu02",0)












