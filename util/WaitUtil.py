#-*- coding: utf-8 -*-
import time


class WaitUtil():

    # 执行过程中的暂停
    def sleep(self,seconds):
        try:
            time.sleep(seconds)
        except Exception,e:
            print str(e)

    # 等待页面元素出现的封装
    def waitWebElement(self,driver,xpathExpression):
        pass