#-*- coding: utf-8 -*-
from selenium import webdriver
import time
import sys
sys.path.append("\util")
from util import Constants
from util import ObjectMap
from util import Log
import logging



class KeyWordsAction():
    objectMap = ObjectMap.ObjcetMap(Constants.Constants.path_configurationFile)
    logging.config.fileConfig("../log.conf")
    driver = None

    @staticmethod
    def open_browser(browserName):
        try:
            if str(browserName).lower() == "ie":
                #或许还要指定驱动
                KeyWordsAction.driver = webdriver.Ie()
                Log.Log.info("IE 实例已经声明")
            elif str(browserName).lower() == "chrome":
                #或许还要指定驱动
                KeyWordsAction.driver = webdriver.Chrome()
                Log.Log.info("Chorme 实例已经声明")
            elif str(browserName).lower() == "firefox":
                #或许还要指定驱动
                KeyWordsAction.driver = webdriver.Firefox()
                Log.Log.info("Firefox 实例已经声明")
        except Exception,e:
            Log.Log.info("浏览器实例已经声明异常")
            print str(e)

    @staticmethod
    def navigate(url):
        try:
            KeyWordsAction.driver.get(url)
            Log.Log.info("访问URL:%s" %(url))
        except Exception,e:
            Log.Log.info("访问URL:%s异常" %(url))
            print str(e)

    @staticmethod
    def input_keyWord(keyWord):
        try:
            KeyWordsAction.driver.find_element(by=KeyWordsAction.objectMap.getLocator("baidu","mainPage.searchBox")[0],value=KeyWordsAction.objectMap.getLocator("baidu","mainPage.searchBox")[1]).clear()
            KeyWordsAction.driver.find_element(by=KeyWordsAction.objectMap.getLocator("baidu","mainPage.searchBox")[0],value=KeyWordsAction.objectMap.getLocator("baidu","mainPage.searchBox")[1]).send_keys(keyWord)
            Log.Log.info("在输入框输入%s" %(keyWord))
        except Exception,e:
            Log.Log.info("在输入框输入%s异常" %(keyWord))
            print str(e)

    @staticmethod
    def click_search(value):
        try:
            KeyWordsAction.driver.find_element(by=KeyWordsAction.objectMap.getLocator("baidu","homePage.sarchButton")[0],value=KeyWordsAction.objectMap.getLocator("baidu","homePage.sarchButton")[1]).click()
            Log.Log.info("点击搜索按钮")
        except Exception,e:
            Log.Log.info("点击搜索按钮异常")
            print str(e)


    @staticmethod
    def waitfor_element(elementExpress):
        try:
            KeyWordsAction.driver.implicitly_wait(10)
            KeyWordsAction.driver.find_element(by=KeyWordsAction.objectMap.getLocator("baidu",elementExpress)[0],value=KeyWordsAction.objectMap.getLocator("baidu",elementExpress)[1])
            Log.Log.info("智能等待")
        except Exception,e:
            Log.Log.info("智能等待异常")
            print str(e)

    @staticmethod
    def assertIn(testcase,assertString):
        try:
            testcase.assertTrue(assertString in KeyWordsAction.driver.page_source)
        except AssertionError ,msg:
            print msg

    @staticmethod
    def sleep(second):
        try:
            time.sleep(second)
            Log.Log.info("睡觉%d秒" %(second))
        except Exception,e:
            Log.Log.info("睡觉%d秒异常" %(second))
            print str(e)


    @staticmethod
    def close_browser(value):
        try:
            KeyWordsAction.driver.quit()
            Log.Log.info("关闭浏览器")
        except Exception,e:
            Log.Log.info("关闭浏览器y异常")
            print str(e)





if __name__ == "__main__":
    KeyWordsAction.driver = webdriver.Chrome()
    KeyWordsAction.navigete("https://www.baidu.com")
    KeyWordsAction.input_keyWord("haha")
