 #-*- coding: utf-8 -*-
import logging
import logging.config


class Log():



    logger = logging.getLogger("infoLogger")


    @staticmethod
    def startTestCase(testCaseName):
        Log.logger.info("----------------------%s开始执行----------------------" %(testCaseName))


    @staticmethod
    def endTestCase(testCaseName):
        Log.logger.info("----------------------%s结束执行----------------------" %(testCaseName))

    @staticmethod
    def info(message):
        Log.logger.info(message)

    @staticmethod
    def error(message):
        Log.logger.error(message)

    @staticmethod
    def debug(message):
        Log.logger.debug(message)