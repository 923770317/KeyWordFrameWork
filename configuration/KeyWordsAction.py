#-*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import sys
sys.path.append("\util")
from util import Constants
from util import ObjectMap



class KeyWordsAction():
    objectMap = ObjectMap.ObjcetMap(Constants.Constants.path_configurationFile)
    driver = None

    @staticmethod
    def open_browser(browserName):
        try:
            if str(browserName).lower() == "ie":
                #或许还要指定驱动
                KeyWordsAction.driver = webdriver.Ie()
            elif str(browserName).lower() == "chrome":
                #或许还要指定驱动
                KeyWordsAction.driver = webdriver.Chrome()
            elif str(browserName).lower() == "firefox":
                #或许还要指定驱动
                KeyWordsAction.driver = webdriver.Firefox()
        except Exception,e:
            print str(e)

    @staticmethod
    def navigate(url):
        try:
            KeyWordsAction.driver.get(url)
        except Exception,e:
            print str(e)

    @staticmethod
    def input_keyWord(keyWord):
        try:
            KeyWordsAction.driver.find_element(by=KeyWordsAction.objectMap.getLocator("baidu","mainPage.searchBox")[0],value=KeyWordsAction.objectMap.getLocator("baidu","mainPage.searchBox")[1]).clear()
            KeyWordsAction.driver.find_element(by=KeyWordsAction.objectMap.getLocator("baidu","mainPage.searchBox")[0],value=KeyWordsAction.objectMap.getLocator("baidu","mainPage.searchBox")[1]).send_keys(keyWord)
        except Exception,e:
            print str(e)

    @staticmethod
    def click_search(value):
        try:
            KeyWordsAction.driver.find_element(by=KeyWordsAction.objectMap.getLocator("baidu","homePage.sarchButton")[0],value=KeyWordsAction.objectMap.getLocator("baidu","homePage.sarchButton")[1]).click()
        except Exception,e:
            print str(e)


    @staticmethod
    def waitfor_element(elementExpress):
        try:
            KeyWordsAction.driver.implicitly_wait(10)
            KeyWordsAction.driver.find_element(by=KeyWordsAction.objectMap.getLocator("baidu",elementExpress)[0],value=KeyWordsAction.objectMap.getLocator("baidu",elementExpress)[1])
        except Exception,e:
            print str(e)

    @staticmethod
    def assert_string(assertString):
        try:



    @staticmethod
    def close_browser(value):
        KeyWordsAction.driver.quit()






if __name__ == "__main__":
    KeyWordsAction.driver = webdriver.Chrome()
    KeyWordsAction.navigete("https://www.baidu.com")
    KeyWordsAction.input_keyWord("haha")
