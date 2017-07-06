#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


class KeyBoardUtil():

    def __init__(self,driver):
        self.driver = driver

    # 按Tab键
    def pressTabKey(self,element):
        try:
            element.send_keys(Keys.TAB)
        except Exception,e:
            print str(e)

    # 按回车键
    def pressEnterKey(self,element):
        try:
            element.send_keys(Keys.ENTER)
        except Exception,e:
            print str(e)

    # 指定字符串为剪切板的内容，然后执行粘贴操作
    def setAndCtrlVClipboardData(self,element,charString):
        try:
            element.send_keys(Keys.CONTROL ,'v')
        except Exception,e:
            print str(e)



if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    time.sleep(3)
    element = driver.find_element(by = By.ID,value = "kw")
    keyBoard = KeyBoardUtil(driver)
    keyBoard.pressEnterKey(element)
    driver.fin
