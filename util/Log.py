 #-*- coding: utf-8 -*-
import logging
import logging.config

class Log():

    logger = logging.getLogger()


    @staticmethod
    def startTestCase(testCaseName):
        Log.logger.info("----------------------\"",testCaseName," \"开始执行 ----------------------")


    @staticmethod
    def endTestCase(testCaseName):
        Log.logger.info("----------------------\"",testCaseName," \"结束执行 ----------------------")

    @staticmethod
    def info(message):
        Log.logger.info(message)

    @staticmethod
    def error(message):
        Log.logger.error(message)

    @staticmethod
    def debug(message):
        Log.logger.debug(message)