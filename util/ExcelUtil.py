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
    def getCellData(sheetName,rowNum,colNum):
        try:
            ExcelUtil.excelBook = ExcelUtil.excelSheet.sheet_by_name(sheetName)
            cellData = ExcelUtil.excelBook.cell(rowNum,colNum).value
            return cellData
        except Exception,e:
            print str(e)


    @staticmethod
    def getLastRowNum(sheetName):
        try:
            ExcelUtil.excelBook = ExcelUtil.excelSheet.sheet_by_name(sheetName)
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



    @staticmethod
    def getRowCount(sheetName):
        try:
            ExcelUtil.excelBook = ExcelUtil.excelSheet.sheet_by_name(sheetName)
            number = ExcelUtil.getLastRowNum(sheetName)
            return number
        except Exception,e:
            print str(e)



    @staticmethod
    def getFirstRowContainsTestCaseId(sheetName,testCaseName,colNum):
        try:
            ExcelUtil.excelBook = ExcelUtil.excelSheet.sheet_by_name(sheetName)
            flag = False
            rowNum = ExcelUtil.getRowCount(sheetName)
            for i in range(1,rowNum):
                if str(ExcelUtil.getCellData(sheetName,i,colNum)).lower() == testCaseName:
                    flag = True
                    return i
            if(flag == False):
                raise Exception("么有")
        except Exception,e:
            print str(e)



    @staticmethod
    def getTestCaseLastStepRow(sheetName,testCaseId,testCaseStartRowNum):
        try:
            ExcelUtil.excelBook = ExcelUtil.excelSheet.sheet_by_name(sheetName)
            rowNum = ExcelUtil.getRowCount(sheetName)
            for i in range(testCaseStartRowNum,rowNum):
                if not str(ExcelUtil.getCellData(sheetName,i,Constants.Constants.Col_TestCaseID)).lower() == testCaseId :
                    return i
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












